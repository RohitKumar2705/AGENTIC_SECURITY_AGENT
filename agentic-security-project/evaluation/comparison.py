import pandas as pd
def create_comparison_dataframe(results):
    dataframe = pd.DataFrame(results)
    return dataframe

def calculate_agent_summary(dataframe):
    summary = dataframe.groupby(
        "agent",

    ).agg(
        average_accuracy=("accuracy", "mean"),
        average_latency=("latency", "mean")
    )

    return summary.reset_index()