import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def call_chat_completion(question: str):
    chat_completion = openai.ChatCompletion.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="gpt-4",
    )
    return chat_completion.choices[0].message['content']