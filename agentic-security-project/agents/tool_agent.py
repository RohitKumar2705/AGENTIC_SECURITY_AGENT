
    
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from openai import OpenAI

from config.settings import OPENAI_API_KEY, MODEL_NAME

from tools.vulnerability_lookup import lookup_vulnerability
from tools.risk_calculator import calculate_risk
from tools.config_analyzer import analyze_configuration

client = OpenAI(api_key=OPENAI_API_KEY)

def select_tool(test_case: dict):


 category = test_case.get("category")

 if category == "vulnerability_lookup":
    return "vulnerability_lookup"

 elif category == "risk_calculation":
    return "risk_calculator"

 elif category == "configuration_analysis":
    return "config_analyzer"

 return "no_tool"


def execute_tool(test_case: dict, tool_name: str):


 if tool_name == "vulnerability_lookup":

    return lookup_vulnerability(
        software=test_case.get("software"),
        version=test_case.get("version")
    )

 elif tool_name == "risk_calculator":

    values = test_case.get("risk_values", {})

    return calculate_risk(
        impact=values.get("impact"),
        likelihood=values.get("likelihood")
    )

 elif tool_name == "config_analyzer":

    return analyze_configuration(
        test_case.get("configuration")
    )

 return None


def run_tool_agent(test_case: dict):
    tool_name = select_tool(test_case)
    tool_result = None

    if tool_name != "no_tool":
        tool_result = execute_tool(test_case, tool_name)

    prompt = f"""
You are an AI agent participating in an academic
security-analysis experiment.

This is an authorized and controlled laboratory scenario.

Task:
{test_case}

Selected tool:
{tool_name}

Tool result:
{tool_result}

Use the provided tool result when available.

Provide:

1. Security analysis
2. Risk level
3. Explanation
4. Defensive recommendation

Do not claim to have scanned a real system.
Do not invent information that is not present in the task
or tool result.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a security analysis agent operating "
                    "only in authorized laboratory environments."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return {
        "response": response.choices[0].message.content,
        "tool_used": tool_name,
        "tool_result": tool_result
    }

