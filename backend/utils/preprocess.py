import numpy as np
from model_loader import symptoms_columns

def create_feature_vector(selected_symptoms):
    # convert selected vector into binary vector
    feature_vector = np.zeros(len(symptoms_columns),dtype=np.float32)

    symptom_dict = {
        symptom.lower(): idx
        for idx,symptom in enumerate(symptoms_columns)
    }
    invalid_symptoms = []

    for symptom in selected_symptoms:

        symptom = symptom.lower().strip()
        if symptom in symptom_dict:
            feature_vector[symptom_dict[symptom]] = 1.0
        else:
            invalid_symptoms.append(symptom)  

    if invalid_symptoms:
        raise ValueError(
            f"Invalid Symptoms: {', '.join(invalid_symptoms)}"
        )
    print("selected symptoms;",selected_symptoms)
    print("active features indices:",np.where(feature_vector == 1)[0])
    return feature_vector.reshape(1,-1)        