import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from agents.pure_llm_agent import run_pure_llm_agent
from agents.tool_agent import run_tool_agent
from evaluation.accuracy import calculate_keyword_accuracy
from evaluation.comparison import (
    calculate_agent_summary,
    create_comparison_dataframe,
)
from evaluation.latency import measure_latency


DATA_PATH = BASE_DIR / "data" / "ground_truth.json"
RESULTS_PATH = BASE_DIR / "results" / "csv" / "experiment_results.csv"
GRAPHS_PATH = BASE_DIR / "results" / "graphs"


def load_test_cases():
    with DATA_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def create_graphs(summary):
    GRAPHS_PATH.mkdir(parents=True, exist_ok=True)

    plt.figure()
    plt.bar(summary["agent"], summary["average_accuracy"])
    plt.title("Average Accuracy Comparison")
    plt.xlabel("Agent")
    plt.ylabel("Average Accuracy")
    plt.savefig(GRAPHS_PATH / "accuracy_comparison.png")
    plt.close()

    plt.figure()
    plt.bar(summary["agent"], summary["average_latency"])
    plt.title("Average Latency Comparison")
    plt.xlabel("Agent")
    plt.ylabel("Latency (Seconds)")
    plt.savefig(GRAPHS_PATH / "latency_comparison.png")
    plt.close()


def run_experiment():
    test_cases = load_test_cases()
    all_results = []
    print("Starting agent comparison")

    for test_case in test_cases:
        test_id = test_case["id"]
        expected_keywords = test_case.get("expected_keywords", [])
        print(f"Running test case {test_id}")

        pure_result = measure_latency(run_pure_llm_agent, test_case)
        pure_accuracy = calculate_keyword_accuracy(
            pure_result["result"], expected_keywords
        )
        all_results.append(
            {
                "test_id": test_id,
                "category": test_case.get("category", "unknown"),
                "agent": "Pure LLM",
                "accuracy": pure_accuracy["accuracy"],
                "latency": pure_result["latency_seconds"],
                "tool_used": "None",
                "matched_keywords": ", ".join(
                    pure_accuracy["matched_keywords"]
                ),
            }
        )

        tool_result = measure_latency(run_tool_agent, test_case)
        tool_output = tool_result["result"]
        tool_accuracy = calculate_keyword_accuracy(
            tool_output["response"], expected_keywords
        )
        all_results.append(
            {
                "test_id": test_id,
                "category": test_case.get("category", "unknown"),
                "agent": "Tool Agent",
                "accuracy": tool_accuracy["accuracy"],
                "latency": tool_result["latency_seconds"],
                "tool_used": tool_output["tool_used"],
                "matched_keywords": ", ".join(
                    tool_accuracy["matched_keywords"]
                ),
            }
        )

    dataframe = create_comparison_dataframe(all_results)
    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(RESULTS_PATH, index=False)
    print(f"\nExperiment results saved: {RESULTS_PATH}")

    summary = calculate_agent_summary(dataframe)
    print("\nAgent performance summary:\n")
    print(summary)
    create_graphs(summary)
    print(f"\nGraphs created: {GRAPHS_PATH}")


if __name__ == "__main__":
    run_experiment()
