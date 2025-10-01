import json
import os
import time
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pydantic import BaseModel
from typing import List
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from testPlan import process_target_data
from dotenv import load_dotenv
from email_utils import send_results_email
from jira_utils import create_jira_issue, attach_file_to_issue
from trello_utils import create_trello_card, attach_file_to_card

load_dotenv(".env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# -----------------------------
# Data Schemas
# -----------------------------
class TestCase(BaseModel):
    id: str
    suite: str
    steps: List[str]
    expected: str
    priority: str

class TestPlan(BaseModel):
    website: str
    suites: List[str]
    cases: List[TestCase]


# -----------------------------
# Website Sampler
# -----------------------------
def sample_links(url: str, num_tests: int = 5, depth: int = 1) -> List[str]:
    options = Options()
    options.headless = True
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    visited = set()
    to_visit = [(url, 0)]
    links = []

    while to_visit and len(links) < num_tests:
        current_url, current_depth = to_visit.pop(0)
        if current_url in visited or current_depth > depth:
            continue
        try:
            driver.get(current_url)
            time.sleep(2)
        except Exception:
            continue

        visited.add(current_url)
        elements = driver.find_elements(By.TAG_NAME, 'a')
        for elem in elements:
            link = elem.get_attribute('href')
            if link and link.startswith('http') and link not in links:
                links.append(link)
                if current_depth + 1 <= depth:
                    to_visit.append((link, current_depth + 1))
            if len(links) >= num_tests:
                break

    driver.quit()
    return links


# -----------------------------
# LLM Planner
# -----------------------------
def extract_full_html(url: str) -> str:
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    driver.quit()
    return html


def generate_testplan(url: str, links: List[str]) -> TestPlan:
    page_html = extract_full_html(url)

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=OPENAI_API_KEY,
        temperature=0.2
    )

    template = ChatPromptTemplate.from_template("""
        You are an expert QA engineer.  
        Here is the FULL HTML of the target website:  
        {page_html}

        Generate a structured test plan in JSON with:
        - Suites: Smoke, Navigation, Forms
        - Each test case must include: id, suite, steps, expected, priority.
        - Only use elements that are actually present in the HTML.
        - Do NOT invent links, forms, or buttons that are not in the HTML.
        - Make steps clear and actionable (like clicking buttons, filling inputs).
        Return only JSON.
    """)

    prompt = template.format_messages(page_html=page_html)
    response = llm.invoke(prompt)
    plan_json = response.content.strip()
    if plan_json.startswith("```json"):
        plan_json = plan_json.replace("```json", "").replace("```", "").strip()

    try:
        parsed = json.loads(plan_json)
    except json.JSONDecodeError as e:
        print("❌ Failed JSON parsing. Raw LLM output:", plan_json)
        raise ValueError("LLM did not return valid JSON") from e

    cases = []
    if "testPlan" in parsed:
        suites_dict = parsed["testPlan"].get("suites", {})
    else:
        suites_dict = parsed.get("suites", {})

    for suite_name, suite_cases in suites_dict.items():
        for c in suite_cases:
            cases.append(TestCase(**c))

    return TestPlan(website=url, suites=list(suites_dict.keys()), cases=cases)


# -----------------------------
# Save Outputs
# -----------------------------
def save_testplan(plan: TestPlan, base_path: str = "./output"):
    os.makedirs(base_path, exist_ok=True)
    json_path = f"{base_path}/plan.json"
    excel_path = f"{base_path}/Plan.xlsx"

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(plan.dict(), f, indent=2, ensure_ascii=False)

    data = [
        {
            "ID": c.id,
            "Suite": c.suite,
            "Steps": " | ".join(c.steps),
            "Expected": c.expected,
            "Priority": c.priority
        } for c in plan.cases
    ]
    df = pd.DataFrame(data)
    df.to_excel(excel_path, index=False)

    return json_path, excel_path


# -----------------------------
# Planner Runner
# -----------------------------
def run_planner(target: str, num_tests: int = 5, depth: int = 1, email: str = "", pm: str = "jira", project_key: str = None):
    process_target_data(target)

    links = sample_links(target, num_tests=num_tests, depth=depth)
    plan = generate_testplan(target, links)
    json_path, excel_path = save_testplan(plan)

    print(f"✅ Test Plan generated successfully for {target}!")

    if email:
        send_results_email(email, attachments=[json_path, excel_path])
        print(f"📧 Results sent to: {email}")

    print(f"📋 Project Management tool selected: {pm}")

    jira_issue_key = None
    trello_card_id = None

    # -----------------------------
    # Jira Integration
    # -----------------------------
    if pm.lower() == "jira" and project_key:
        summary = f"Test Plan Generated for {target}"
        description = f"Files generated:\n- {json_path}\n- {excel_path}"
        issue = create_jira_issue(summary, description, project_key=project_key)
        if issue:
            jira_issue_key = issue.get("key")
            attach_file_to_issue(jira_issue_key, json_path)
            attach_file_to_issue(jira_issue_key, excel_path)

    # -----------------------------
    # Trello Integration
    # -----------------------------
    elif pm.lower() == "trello":
        card_name = f"Test Plan for {target}"
        card_desc = f"Files generated:\n- {json_path}\n- {excel_path}"
        card = create_trello_card(card_name, card_desc)
        if card:
            trello_card_id = card["id"]
            attach_file_to_card(trello_card_id, json_path)
            attach_file_to_card(trello_card_id, excel_path)

    return {
        "json": json_path,
        "excel": excel_path,
        "jira_issue": jira_issue_key,
        "trello_card": trello_card_id
    }
