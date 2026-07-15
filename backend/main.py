import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from exceptions import global_exception_handler
from schemas import Predictionrequest,PredictionResponse,ChatRequest
from services.predictor import predict_disease
from logger import logger
from config import API_NAME,API_VERSION,DEFAULT_MODEL,DISCLAIMER
from utils.disease_info import get_disease_info,get_all_diseases
from services.llm_service import generate_ai_explaination
from model_loader import symptoms_columns
from services.chat_service import ask_ai




app = FastAPI(title=API_NAME,version=API_VERSION,description="AI_POWERED SYMPTOM ASSISTANT")
app.add_exception_handler(Exception,global_exception_handler)
#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message":"Welcome to tMedical Assitant App",
        "version":API_VERSION,
        "model":DEFAULT_MODEL
    }

@app.post("/predict",response_model=PredictionResponse)
def predict(request:Predictionrequest):
    logger.info(f"Symptoms Recieved: {request.symptoms}")
    start_time = time.time()
    predictions = predict_disease(request.symptoms)
    processing_time = round((time.time() - start_time) * 1000,2)
    top_prediction = predictions[0]
    disease_info = get_disease_info(top_prediction["disease"])
    prediction_for_llm = {
        "disease":top_prediction["disease"],
        "description":disease_info["description"],
        "possible_causes":disease_info["possible_causes"],
        "precautions":disease_info["precautions"],
        "recommended_specialist":disease_info["recommended_specialist"]
    }

    ai_explanation = generate_ai_explaination(
        request.symptoms,
        prediction_for_llm
    )

    logger.info(f"Prediction : {top_prediction}")

    return {
        "success":True,
        "prediction":top_prediction,
        "disease_information":disease_info,
        "ai_explanation":ai_explanation,
        "top_predictions":predictions,
        "processing_time":processing_time,
        "disclaimer":"this tool is just a predictior,not suitable for professional medical advice"
    }

@app.get("/health")
def health():
    return {
        "status":"healthy",
        "api":API_NAME,
        "model":DEFAULT_MODEL
    }

@app.get("/diseases")
def list_diseases():
    diseases = get_all_diseases()
    return {
        "success":True,
        "count":len(diseases),
        "diseases":diseases
        }    
@app.get("/diseases/{disease_name}")
def disease_detail(disease_name:str):
    disease = get_disease_info(disease_name)

    if not disease:
        raise HTTPException(
            status_code=404,
            detail="Disease Not found"
        )
    return {
        "success":True,
        "disease":disease_name,
        "details":disease
    }



@app.get("/symptoms")
def get_symptoms():
    return {
        "success":True,
        "count":len(symptoms_columns),
        "symptoms":sorted(symptoms_columns)

    }


@app.post("/ask-ai")
def ask_followup(request: ChatRequest):

    answer = ask_ai(
        request.disease,
        request.question
    )

    return {
        "answer": answer
    }
