
import os
from dotenv import load_dotenv
from google import genai

# Load secrets from the .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. Check your .env file."
    )

# Create a Gemini API client
client = genai.Client(api_key=api_key)

# Send a small test prompt
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Explain Python in one simple sentence."
)

print("Gemini connection successful!")
print(response.text)
