import os
import json
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from jira import JIRA
from dotenv import load_dotenv

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")
JIRA_DOMAIN = os.getenv("JIRA_DOMAIN")
JIRA_PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY", "CFQA")

PLAN_FILE = "./output/plan.json"
OUTPUT_DIR = "tests"
RESULTS_JSON = "Results.json"
SCREENSHOT_DIR = "./screen/screenshots"

# -----------------------------
# Setup AI
# -----------------------------
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=OPENAI_API_KEY,
    max_tokens=1500
)

prompt_template = ChatPromptTemplate.from_template("""
You are an expert QA engineer.

Convert the following test step into **runnable Python Selenium code** using the provided `driver`.

Rules:
- If this is the first step in the test case, include:
    driver.get("{website}")
  before interacting with the page.
- Use exact selectors from the HTML.
- Priority: ID > Name > Placeholder/Text > CSS Selector > XPath.
- Never call driver.quit() or driver.close().
- Output only raw Python code.
- Capture screenshot if step fails.

Website URL: {website}
Full HTML: {html}
Step: {step}
Expected result: {expected}
""")

# -----------------------------
# Jira Setup
# -----------------------------
jira = JIRA(server=f"https://{JIRA_DOMAIN}", basic_auth=(JIRA_EMAIL, JIRA_TOKEN))

def create_jira_issue(case_result):
    """Create a Jira issue for a test case result."""
    status = case_result["status"]
    summary = f"Test case {case_result['id']} → {status}"
    description = f"Result: {status}\nError: {case_result.get('error')}\nScreenshot: {case_result.get('screenshot')}"

    issue_dict = {
        "project": {"key": JIRA_PROJECT_KEY},
        "summary": summary,
        "description": description,
        "issuetype": {"name": "Bug"}  # تأكد من وجوده في Jira
    }
    try:
        issue = jira.create_issue(fields=issue_dict)
        print(f"✅ Jira issue created: {issue.key}")
    except Exception as e:
        print(f"❌ Failed to create Jira issue: {e}")

# -----------------------------
# AI helper functions
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

def generate_selenium_code(step_text, expected_text, website):
    page_html = extract_full_html(website)
    messages = prompt_template.format_messages(
        step=step_text,
        expected=expected_text,
        website=website,
        html=page_html
    )
    response = llm.invoke(messages)
    return response.content.strip()

# -----------------------------
# Generate Selenium test files
# -----------------------------
def generate_test_files(plan):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    test_files = []
    website = plan.get("website", "")

    for case in plan["cases"]:
        case_id = case["id"]
        steps = case.get("steps", [])
        expected = case.get("expected", "")
        all_code = []

        for step in steps:
            code = generate_selenium_code(step, expected, website)
            all_code.append(code)

        file_path = os.path.join(OUTPUT_DIR, f"{case_id}.py")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n\n".join(all_code))

        test_files.append((case_id, file_path))
        print(f"✅ Generated test file: {file_path}")

    return test_files

# -----------------------------
# Run a single test file
# -----------------------------
def run_test_file(case_id, file_path):
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    result = {"id": case_id, "status": "Pass", "error": None, "screenshot": None}

    try:
        driver = webdriver.Chrome()
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
        exec(code, {"driver": driver, "By": By})

    except Exception as e:
        result["status"] = "Fail"
        result["error"] = str(e)
        try:
            screenshot_path = os.path.join(SCREENSHOT_DIR, f"{case_id}.png")
            driver.save_screenshot(screenshot_path)
            result["screenshot"] = screenshot_path
        except:
            pass

    finally:
        try:
            driver.quit()
        except:
            pass

    return result

# -----------------------------
# Main executor
# -----------------------------
def main():
    with open(PLAN_FILE, "r", encoding="utf-8") as f:
        plan = json.load(f)

    test_files = generate_test_files(plan)
    results = []

    for case_id, file_path in test_files:
        print(f"▶ Running test {case_id} ...")
        result = run_test_file(case_id, file_path)
        results.append(result)
        print(f"✔ {case_id} → {result['status']}")
        create_jira_issue(result)  # رفع كل نتيجة مباشرة إلى Jira

    with open(RESULTS_JSON, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Finished! Results saved in {RESULTS_JSON}")

if __name__ == "__main__":
    main()
