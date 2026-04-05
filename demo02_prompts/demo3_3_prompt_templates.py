# Prompt as Product” (Template + Variables).

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
    """Call LLM"""
    print(f"\n ask_llm()...")
    response = client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content


# Prompt template with variables
# TODO: Define a reusable prompt template with placeholders for variables.
# The template should be for drafting an email response to a customer complaint.
EMAIL_TEMPLATE = """
___
"""


# Reuse same template with different inputs
# TODO: Define different scenarios with variable values to fill the template.
# Provide at least two scenarios with different roles, issues, tones and resolutions. 
scenarios = [
___
]

n = 1
for s in scenarios:
    prompt = EMAIL_TEMPLATE.format(**s)  # Fill template dynamically
    print(f"\n--- Scenario {n}: {s["role"]} ---\n")
    print(ask_llm(prompt))
    n += 1
