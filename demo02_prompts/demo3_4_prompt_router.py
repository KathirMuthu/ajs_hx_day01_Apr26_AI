# Prompt Library for Agent Behavior.

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
        temperature=0.4
    )
    return response.choices[0].message.content


# Simple router (simulating agent decision).
def route_prompt(user_input: str):
    """Route input to appropriate prompt"""
    print(f"\n route_prompt()...")

    # TODO: Implement a simple routing logic based one keywords in the user input.
    # If the input contains "comlaint", route to a customer support prompt.
    # If the input contains "report", route to a data analysis prompt.
    # For any other input, route to a general assistant prompt.
    # The "user_input" variable must be passed into the prompt tp provide context for the response.
    ___


# Test inputs.
inputs = [
    "Customer complaint about late delivery",
    "Generate a sales report for Q3",
]


for text in inputs:
    prompt = route_prompt(text)
    print(f"\n--- Input: {text} ---\n")
    print(ask_llm(prompt))

