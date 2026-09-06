def calculate_risk(impact:float,likelihood:float):
    """
    simple academic risk calculation.
    Risk_Score = Impact *Likelihood
    
    """
    score = impact * likelihood
    if score >= 60:
        level = "HIGH"

    elif score >=30:
        level = "MEDIUM"


    else:
        level = "LOW"

    return{
        "risk_score":score,
        "risk_level":level
    }        