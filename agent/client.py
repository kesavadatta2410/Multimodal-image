import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Create the client once here.
# Every other module imports this single instance.
# This avoids creating a new connection on every function call.
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GROQ_API_KEY environment variable is required")
client = Groq(api_key=api_key)