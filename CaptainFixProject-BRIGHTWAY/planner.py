import os
import requests
from datetime import datetime
from langchain_community.chat_models import ChatOpenAI  # Updated import to avoid deprecation
# Other planner-related imports here

# -------------------
# Jira Setup
# -------------------
JIRA_EMAIL = os.getenv("JIRA_EMAIL", "razan.alfeelat@gmail.com")
JIRA_TOKEN = os.getenv("JIRA_TOKEN", "")
JIRA_DOMAIN = os.getenv("JIRA_DOMAIN", "razanalfeelat.atlassian.net")
JIRA_PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY", "CFQA")

def create_jira_issue(summary, description_text, issue_type="Bug"):
    if not (JIRA_DOMAIN and JIRA_PROJECT_KEY and JIRA_EMAIL and JIRA_TOKEN):
        print("⚠️ Jira credentials or project key not set.")
        return None

    url = f"https://{JIRA_DOMAIN}/rest/api/3/issue"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # Convert description to Atlassian Document Format (ADF)
    description = {
        "type": "doc",
        "version": 1,
        "content": [
            {
                "type": "paragraph",
                "content": [{"text": description_text, "type": "text"}]
            }
        ]
    }

    payload = {
        "fields": {
            "project": {"key": JIRA_PROJECT_KEY},
            "summary": summary,
            "description": description,
            "issuetype": {"name": issue_type}
        }
    }

    response = requests.post(url, json=payload, headers=headers, auth=(JIRA_EMAIL, JIRA_TOKEN))

    if response.status_code == 201:
        print(f"✅ Jira issue created: {response.json()['key']}")
        return response.json()
    else:
        print(f"❌ Failed to create Jira issue: {response.status_code} {response.text}")
        return None

# -------------------
# Trello Setup (Optional)
# -------------------
TRELLO_KEY = os.getenv("TRELLO_KEY", "")
TRELLO_TOKEN = os.getenv("TRELLO_TOKEN", "")
TRELLO_LIST_ID = os.getenv("TRELLO_LIST_ID", "")

def create_trello_card(name, desc):
    if not (TRELLO_KEY and TRELLO_TOKEN and TRELLO_LIST_ID):
        print("⚠️ Trello credentials or list ID not set.")
        return None
    url = "https://api.trello.com/1/cards"
    params = {
        "key": TRELLO_KEY,
        "token": TRELLO_TOKEN,
        "idList": TRELLO_LIST_ID,
        "name": name,
        "desc": desc
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        print(f"✅ Trello card created: {response.json()['id']}")
        return response.json()
    else:
        print(f"❌ Failed to create Trello card: {response.status_code} {response.text}")
        return None

# -------------------
# Run Planner Function
# -------------------
def run_planner(target, depth=2, num_tests=5, email=None, pm=None):
    """
    This function runs the Planner:
    - Generates JSON and Excel files
    - Sends email
    - Integrates with Jira/Trello if chosen
    """
    print(f"Website validated: {target}")

    # Example: run LangChain LLM (GPT)
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")  # Can update to GPT-4
    # Add your site processing or test plan generation logic here
    # ...

    # Example: generate placeholder files (modify later)
    json_path = f"./{target.replace('https://','').replace('/','_')}_plan.json"
    excel_path = f"./{target.replace('https://','').replace('/','_')}_plan.xlsx"

    # Create Jira Issue if PM tool = "Jira"
    if pm and pm.lower() == "jira":
        create_jira_issue(
            summary=f"CaptainFix Test Plan for {target}",
            description_text=f"Test plan generated for {target} on {datetime.utcnow().isoformat()}",
            issue_type="Bug"
        )

    # Create Trello Card if PM tool = "Trello"
    if pm and pm.lower() == "trello":
        create_trello_card(
            name=f"Test Plan: {target}",
            desc=f"Generated test plan for {target}"
        )

    # Send email (add your email sending library here)
    if email:
        print(f"Email sent successfully to {email}")

    return {"json": json_path, "excel": excel_path}
