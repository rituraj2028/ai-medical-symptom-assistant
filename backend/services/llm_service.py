import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
print(API_KEY)
if not API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")
client = Groq(api_key=API_KEY)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROMPT_PATH = os.path.join(
    BASE_DIR,
    "prompts",
    "medical_prompt.txt"
)

def load_prompt():
    with open(PROMPT_PATH,"r",encoding="utf-8") as f:
        return f.read()

def generate_ai_explaination(symptoms,prediction):
    prompt = load_prompt().format(
        symptoms=", ".join(symptoms),
        disease = prediction["disease"],
        description = prediction["description"],
        causes = ", ".join(prediction["possible_causes"]),
        precautions=", ".join(prediction["precautions"]),
        specialist = prediction["recommended_specialist"]
    )



    completion = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = [
            {
                "role":"system",
                "content":"you are a medical ai assistant "
            },
            {
                "role":"user",
                "content":prompt
            }
        ],
        temperature=0.3,
        max_tokens=500
    )
    
    return completion.choices[0].message.content