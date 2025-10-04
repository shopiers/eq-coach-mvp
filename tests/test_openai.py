import os
from openai import OpenAI
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Initialize client with your key from .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Make a simple test call
response = client.chat.completions.create(
    model="gpt-4",  # or "gpt-3.5-turbo", depending on your access
    messages=[
        {"role": "user", "content": "Write a haiku about autumn leaves"}
    ]
)

print(response.choices[0].message.content)