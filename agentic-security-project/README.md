# Tool Use vs Pure LLM Reasoning

## Project Overview

This project compares two AI agent architectures for controlled vulnerability analysis:

1. Pure LLM Reasoning
2. Tool-Augmented LLM Agent

The goal is to evaluate when external tool usage improves:

* Accuracy
* Reliability
* Latency
* Reasoning performance

## Project Architecture

### Pure LLM Agent

Task
↓
LLM
↓
Response

### Tool-Augmented Agent

Task
↓
Tool Selection
↓
Local Analysis Tool
↓
LLM Reasoning
↓
Response

## Running the Project

Install dependencies:

pip install -r requirements.txt

Add your API key to `.env`.

Run the experiment:

python experiments/run_experiment.py

## Results

Results are saved inside:

results/csv/

Graphs are saved inside:

results/graphs/

## Safety

This project uses controlled datasets and authorized laboratory scenarios. It does not scan arbitrary real-world systems.
