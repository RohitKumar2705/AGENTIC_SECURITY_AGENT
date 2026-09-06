# Tool Use vs Pure LLM Reasoning in Security Analysis

## Project Overview

This project is an Agentic AI research and development project that compares two different approaches to solving controlled security vulnerability analysis tasks:

1. **Pure LLM Reasoning**
2. **Tool-Augmented LLM Agent**

The main objective of the project is to understand when an AI agent should rely on its own reasoning and when it should use external tools to obtain more accurate, structured, or verifiable information.

The project evaluates whether tool usage improves an AI system's performance and whether the improvement is worth the additional complexity, latency, and computational cost.

---

## Research Question

The main research question of this project is:

> **When does external tool usage improve the performance of an LLM-based agent compared to pure LLM reasoning?**

The project compares both approaches across different types of controlled security-analysis tasks.

---

# Project Architecture

## 1. Pure LLM Agent

The Pure LLM Agent receives a task and generates a response using only the information available in its prompt and its internal reasoning.

```text
Input Task
    │
    ▼
Pure LLM Agent
    │
    ▼
Reasoning
    │
    ▼
Security Analysis
```

The Pure LLM Agent does not access external tools, databases, or live systems.

---

## 2. Tool-Augmented Agent

The Tool-Augmented Agent can use specialized local tools to help analyze a task.

```text
Input Task
    │
    ▼
Tool Selection
    │
    ├── Vulnerability Lookup
    ├── Risk Calculator
    └── Configuration Analyzer
    │
    ▼
LLM Reasoning
    │
    ▼
Security Analysis
```

The agent combines structured tool output with LLM reasoning to generate its final response.

---

# Project Features

The project currently includes:

* Pure LLM reasoning agent
* Tool-augmented AI agent
* Local vulnerability knowledge lookup
* Risk calculation tool
* Configuration analysis tool
* Controlled test scenarios
* Accuracy evaluation
* Latency measurement
* Agent comparison
* CSV experiment results
* Performance visualization graphs
* FastAPI backend

---

# Tools Used by the Agent

## Vulnerability Lookup Tool

The vulnerability lookup tool searches a controlled local vulnerability dataset.

It can provide information such as:

* Software name
* Affected version
* Severity
* Vulnerability description
* Defensive recommendation

This allows the project to evaluate whether access to structured information improves the quality of the agent's analysis.

---

## Risk Calculator

The risk calculator calculates a simple academic risk score.

```text
Risk Score = Impact × Likelihood
```

The calculated score is classified into:

* LOW
* MEDIUM
* HIGH

This tool helps compare LLM reasoning with structured computational results.

---

## Configuration Analyzer

The configuration analyzer checks controlled lab configurations for predefined security issues.

Examples include:

* TLS disabled
* Default credentials enabled
* Administrative interface exposed

The tool returns structured findings that are then interpreted by the LLM agent.

---

# Experimental Workflow

Both agents receive the same test cases.

```text
                    TEST CASE
                        │
            ┌───────────┴───────────┐
            │                       │
            ▼                       ▼
      Pure LLM Agent         Tool-Augmented Agent
            │                       │
            │                 Tool Selection
            │                       │
            │              ┌────────┼────────┐
            │              │        │        │
            │          Lookup     Risk    Config
            │              │        │        │
            └──────────────┴────────┴────────┘
                        │
                        ▼
                   Evaluation
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
       Accuracy       Latency      Tool Usage
                        │
                        ▼
                     Results
```

---

# Evaluation Metrics

The performance of both agents is evaluated using the following metrics.

## Accuracy

The response is compared with expected keywords from the ground-truth dataset.

```text
Accuracy = Matched Expected Keywords / Total Expected Keywords
```

---

## Latency

Latency measures the time required by each agent to generate a response.

```text
Start Time
    │
    ▼
Agent Processing
    │
    ▼
Final Response
```

The project compares whether tool usage improves accuracy at the cost of additional processing time.

---

## Tool Usage

The Tool-Augmented Agent records:

* Which tool was selected
* Whether a tool was required
* Tool output used during reasoning

This helps analyze the efficiency of tool usage.

---

# Project Structure

```text
agentic-security-project/
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── test_cases.json
│   ├── ground_truth.json
│   └── vulnerability_database.json
│
├── agents/
│   ├── __init__.py
│   ├── pure_llm_agent.py
│   └── tool_agent.py
│
├── tools/
│   ├── __init__.py
│   ├── vulnerability_lookup.py
│   ├── risk_calculator.py
│   └── config_analyzer.py
│
├── evaluation/
│   ├── __init__.py
│   ├── accuracy.py
│   ├── latency.py
│   └── comparison.py
│
├── experiments/
│   └── run_experiment.py
│
├── results/
│   ├── csv/
│   └── graphs/
│
├── api/
│   ├── __init__.py
│   └── main.py
│
├── config/
│   └── settings.py
│
├── tests/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Move into the project directory:

```bash
cd agentic-security-project
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

### Windows

```bash
.\venv\Scripts\Activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_api_key_here
```

Do not upload the `.env` file to GitHub.

---

# Running the Experiment

Run the experiment from the project root:

```bash
python experiments/run_experiment.py
```

The experiment will:

1. Load the test cases
2. Run the Pure LLM Agent
3. Run the Tool-Augmented Agent
4. Measure latency
5. Calculate accuracy
6. Compare both agents
7. Save the results
8. Generate performance graphs

---

# Results

Experiment results are saved in:

```text
results/csv/experiment_results.csv
```

Performance graphs are saved in:

```text
results/graphs/
```

The project generates comparisons for:

* Average accuracy
* Average latency
* Agent performance

---

# API

The project also provides a FastAPI backend.

Start the API using:

```bash
uvicorn api.main:app --reload
```

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

The available endpoints include:

```text
POST /pure-agent
POST /tool-agent
```

---

# Example Research Hypothesis

The project is based on the following hypothesis:

> Tool-augmented LLM agents may outperform pure LLM reasoning on tasks that require structured information, calculations, or external knowledge. However, tool usage may increase latency and system complexity.

The experiment is designed to test this hypothesis using controlled security-analysis scenarios.

---

# Future Improvements

Future versions of this project can include:

* LLM-based dynamic tool selection
* More security-analysis tools
* Larger evaluation datasets
* Better ground-truth evaluation
* Semantic similarity evaluation
* LLM-as-a-judge evaluation
* Tool-use efficiency metrics
* Token and API cost tracking
* Reliability testing with multiple experiment runs
* Statistical significance testing
* Interactive frontend dashboard
* LangGraph-based agent orchestration
* Integration with trusted and authorized vulnerability datasets

---

# Safety and Scope

This project is designed for:

* Academic research
* Agentic AI experimentation
* Controlled datasets
* Synthetic scenarios
* Authorized laboratory environments

The project does not perform scanning or analysis of arbitrary real-world systems.

---

# Key Learning Outcomes

By completing this project, the developer will gain experience with:

* Agentic AI architecture
* LLM reasoning
* Tool-augmented agents
* Tool selection and routing
* API integration
* Experiment design
* AI system evaluation
* Latency measurement
* Accuracy comparison
* FastAPI
* Python project architecture
* Data-driven AI research

---

# Conclusion

This project explores an important question in Agentic AI:

> **Should an AI agent solve a problem using reasoning alone, or should it use tools?**

By comparing a Pure LLM Agent with a Tool-Augmented Agent, the project provides a structured framework for evaluating the advantages and trade-offs of tool use in AI systems.

The goal is not simply to build an AI agent that uses tools, but to understand **when tool usage actually provides measurable value**.
