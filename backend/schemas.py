from typing import List
from pydantic import BaseModel,Field
class Predictionrequest(BaseModel):
    symptoms:List[str]=Field(
        ...,
        min_length =1,
        description="List of Symptoms Selected by the User"
    )

class DiseasePrediction(BaseModel):
    disease: str
    confidence:float

class DiseaseInformation(BaseModel):
    description:str
    possible_causes: List[str]
    precautions: List[str]
    recommended_specialist:str    

class PredictionResponse(BaseModel):
    success: bool
    prediction:DiseasePrediction
    top_predictions:List[DiseasePrediction]
    ai_explanation:str
    disease_information:DiseaseInformation
    disclaimer:str        
    processing_time:float
   
class ChatRequest(BaseModel):
    disease: str 
    question:str  

class ChatResponse(BaseModel):
    answer : str    