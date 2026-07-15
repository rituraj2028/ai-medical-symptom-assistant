import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
JSON_PATH  = os.path.join(BASE_DIR,"data","diseases.json")

with open(JSON_PATH,"r",encoding="utf-8") as f:
    DISEASE_INFO = json.load(f)

def get_disease_info(disease_name:str):

    return DISEASE_INFO.get(disease_name.lower(),{})    


def get_all_diseases():
    return sorted(DISEASE_INFO.keys())    