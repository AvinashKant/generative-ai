import google.generativeai as genai
import os

# 🔑 Set your Gemini API Key
# Option 1: Environment variable (recommended)
# export GOOGLE_API_KEY="your_api_key_here"

# Option 2: Direct assignment (not recommended for production)
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY") or "YOUR_API_KEY_HERE"
#GOOGLE_API_KEY = ""
print("Using API Key:-", GOOGLE_API_KEY)

genai.configure(api_key='GOOGLE_API_KEY')


MODEL_NAME = "gemini-2.5-flash"

SYSTEM_PROMPT = """
You are a helpful AI agent.
Answer clearly and concisely.
"""

class FastGeminiAgent:
    def __init__(self):
        self.model = genai.GenerativeModel(
            model_name=MODEL_NAME,
            system_instruction=SYSTEM_PROMPT
        )

    def generate(self, user_input):
        response = self.model.generate_content(
            user_input,
            generation_config={
                "temperature": 0.5,
                "max_output_tokens": 300
            }
        )
        return response.text.strip()


def run_agent():
    if GOOGLE_API_KEY == "AIzaSyCpiTLz5SRJR_yHDiEye-NetbFQLKMNnGU":
        print("Error: Please set your Gemini API key in the previous cell (cell Umtu7hPNlhl8).")
        print("You can get an API key from https://aistudio.google.com/app/apikey")
        return

    agent = FastGeminiAgent()
    print("⚡ Fast AI Agent (Gemini). Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in {"quit", "exit"}:
            print("Agent: Goodbye 👋")
            break

        reply = agent.generate(user_input)
        print("Agent:", reply, "\n")


if __name__ == "__main__":
    run_agent()