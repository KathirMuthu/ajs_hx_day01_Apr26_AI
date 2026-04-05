# Build a 3-Scenario Prompt Library.

# Set env vars from config.py.
import sys
import os

# Add the folder path (use absolute or relative path)
folder_path = os.path.join(os.path.dirname(__file__), '../')
sys.path.insert(0, folder_path)

import config

# Start.
from dotenv import load_dotenv
import os
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")


def ask_llm(prompt: str):
    """Reusable function to call LLM"""
    print(f"\n ask_llm()...")
    response = client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content


# TODO: Create a Prompt Library with 3 business scenarios.
# 1. Customer support: draft a response to a complaint about late delivery.
# 2. Data analysis: summarize sales data into key insights. Provide some sample sales data in the prompt.
# 3. Meeting notes: extract key decisions and action items from meeting notes. Provide sample meeting notes.
PROMPT_LIBRARY = {

    "email_response": """
    ___
    """,

    "data_summary": """
    ___
    """,

    "meeting_summary": """
    ___
    """
}


# TODO: Iterate through the Prompot Library.
# Call the ask_llm() for each scenario and print the output.
___

