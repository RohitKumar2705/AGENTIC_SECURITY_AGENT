import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from fastapi import FastAPI

from agents.pure_llm_agent import run_pure_llm_agent
from agents.tool_agent import run_tool_agent

app = FastAPI(
title="Agentic Security Research API"
)

@app.get("/")
def home():


 return {
    "message": (
        "Agentic Security Research API"
    )
}


@app.post("/pure-agent")
def pure_agent(
test_case: dict
):


 response = (
    run_pure_llm_agent(
        test_case
    )
)

 return {
    "agent": "Pure LLM",
    "response": response
}


@app.post("/tool-agent")
def tool_agent(
test_case: dict
):


 result = (
    run_tool_agent(
        test_case
    )
)

 return {
    "agent": "Tool-Augmented Agent",
    "response": result
}


if __name__ == "__main__":
 import uvicorn

 uvicorn.run(
     app,
     host=os.getenv("HOST", "127.0.0.1"),
     port=int(os.getenv("PORT", "8000"))
 )

