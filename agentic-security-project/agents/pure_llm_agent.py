import sys
from pathlib import Path

from openai import OpenAI

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config.settings import OPENAI_API_KEY, MODEL_NAME

client = OpenAI(api_key = OPENAI_API_KEY)
def run_pure_llm_agent(test_case:dict):
    prompt = f"""
           You are an AI assistant participating in an academic
security-analysis experiment.

Analyze only the information provided in the task.

Do not claim that you accessed external databases,
websites, scanners, or live systems.

This is a controlled and authorized lab scenario.

Task:
{test_case}

Provide:

1.Security analysis
2.Risk level
3.Explanation
4.Defensive recommendation
"""

    response = client.chat.completions.create(
        model = MODEL_NAME,
        messages = [
            {
                "role": "system",
                "content":(
"You are a careful security analysis assistant "
"for authorized laboratory scenarios."
)

                                        },
         {
             "role":"user",
             "content":prompt,
                             }                                
        ],
        temperature = 0

    )
    return response.choices[0].message.content