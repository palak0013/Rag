import google.generativeai as genai
import os
from dotenv import load_dotenv
from google import genai as google_genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize client only when needed
client = google_genai.Client()
