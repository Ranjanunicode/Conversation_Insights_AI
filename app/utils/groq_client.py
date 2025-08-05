# app/utils/groq_client.py
import os
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

async def generate_transcript():
    prompt = (
        "Generate a realistic sales call transcript between a sales agent and a customer "
        "about a product. Keep it around 20-30 lines. Mark each speaker as 'Agent:' or 'Customer:'."
    )
    
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    # model="llama-3.1-8b-instant",
    model="llama-3.3-70b-versatile",
    temperature= 0.7,
)
    response = chat_completion.choices[0].message.content
    return response
