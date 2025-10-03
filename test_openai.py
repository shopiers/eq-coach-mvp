import os
from openai import OpenAI
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Initialize client with your key from .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Make a simple test call
response = client.responses.create(
    model="gpt-5-nano",
    input="Write a haiku about autumn leaves",
)

print(response.output_text)