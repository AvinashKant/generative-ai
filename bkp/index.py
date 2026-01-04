from google import genai

from dotenv import load_dotenv
import os

load_dotenv()  # Reads .env and loads variables into environment
api_key = os.getenv("GEMINI_API_KEY")
print(api_key)

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)