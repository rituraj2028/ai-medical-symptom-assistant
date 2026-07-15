def generate_explanation(prediction):
    disease = prediction["disease"]
    confidence = prediction["confidence"]
    specialist = prediction["recommended_specialist"]
    precautions = prediction["precautions"]

    explanation = (
        f"Based on the symptoms youselected,"
        f"the AI model predicts '{disease}"
        f"with a confidence of {confidence}%"
        f"It is recommended to consult a"
        f"{specialist}"

    )
    if precautions:
        explanation +=(
            "Some general precautions include:"
            +", ".join(precautions[:3])
            +"."
        )
    return explanation