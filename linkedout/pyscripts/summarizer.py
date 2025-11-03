from google import genai
from google.genai import types
from pyscripts.scraper import scrape_data
from environ import Env
from pathlib import Path
import os
env = Env()
BASE_DIR = Path(__file__).resolve().parent.parent.parent
env.read_env(os.path.join(BASE_DIR, '.env'))
client = genai.Client(api_key=env("SALAAR_SENPAI"))

def summarize_text(text):

     response = client.models.generate_content(
         model="gemini-2.5-flash",
         config = types.GenerateContentConfig(
             system_instruction="You are a bot that summarizes linkedin posts into one single line. You know LinkedIn is full of AI slop, so you give only one line summary that is the core of the post. Do mention the name of the writer somewhere in the summary.",
         ),
         contents=f"Summarize this linkedin post written by {text[0]}:\n\n{text[1]}",
     )

     return response.text

if __name__ == "__main__":
    text = scrape_data("https://www.linkedin.com/feed/update/urn:li:activity:7384043929542991872/")
    print(text)
    # summary = summarize_text(text)
    # print(summary)