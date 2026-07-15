import numpy as np
import tensorflow as tf
from model_loader import dnn_model,label_encoder
from utils.preprocess import create_feature_vector
from config import TOP_K
from utils.disease_info import get_disease_info
from services.explanation import generate_explanation

def predict_disease(selected_symptoms):
    input_vector =create_feature_vector(selected_symptoms)

    input_tensor = tf.convert_to_tensor(input_vector,dtype=tf.float32)  

    infer = dnn_model.signatures["serving_default"]

    output = infer(inputs = input_tensor)

    probablities =list(output.values())[0].numpy()[0]

    top_idx = np.argsort(probablities)[-TOP_K:][::-1]

    predictions = []

    for idx in top_idx:
        disease = label_encoder.inverse_transform([idx])[0]
        info = get_disease_info(disease)

        prediction = {
            "disease":disease,
            "confidence":round(float(probablities[idx] * 100),2),
            "description":info.get(
                "description",
                "Information Not Availaible"
            ),

            "possible_causes": info.get(
            "possible_causes","[]"
            ),
            "precautions":info.get(
                "precautions",[]
            ),
            "recommended_specialist":info.get(
                "recommend_specialist",
                "General Physician"
            )
        }
        prediction["explaination"] = generate_explanation(prediction)
        predictions.append(prediction)

    return predictions    