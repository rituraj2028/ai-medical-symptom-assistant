from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_ai(disease, question):

    prompt = f"""
You are an AI medical assistant.

The predicted disease is:

{disease}

The user asks:

{question}

Rules:

- Never claim the disease is confirmed.
- Explain in simple English.
- Keep the answer under 200 words.
- Recommend consulting a doctor.
- Mention emergency care if symptoms become severe.
"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]

    )

    return response.choices[0].message.content
