import os
import sys
import argparse
from google.genai import types, Client
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser(description="Run a prompt for Gemini model.")
parser.add_argument("prompt", type=str, help="The request or prompt to send to the model.")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output.")

args = parser.parse_args()


api_key = os.environ.get("GEMINI_API_KEY")
client = Client(api_key=api_key)

messages = [
    types.Content(
        role="user",
        parts=[types.Part(text=args.prompt)],
    )
]

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages
)

print(response.text)

if args.verbose:
    print("User prompt:", args.prompt)
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)