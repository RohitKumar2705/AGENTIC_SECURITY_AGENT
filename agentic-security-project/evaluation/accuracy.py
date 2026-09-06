def calculate_keyword_accuracy(response:str,expected_keywords:list):
    response_lower = response.lower()
    matched_keywords = []

    for keyword in expected_keywords:
        if keyword.lower() in response_lower:
            matched_keywords.append(keyword)


    if not expected_keywords:
        return {
            "accuracy":0.0,
            "matched_keywords":[],

        }   

    accuracy = (len(matched_keywords)/len(expected_keywords)   ) 

    return {
        "accuracy":accuracy,
        "matched_keywords":matched_keywords
    } 

    