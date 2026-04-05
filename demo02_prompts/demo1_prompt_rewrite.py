# Rewrite a Poor Prompt.

# Set env vars from config.py.
import sys
import os

# Add the folder path (use absolute or relative path)
folder_path = os.path.join(os.path.dirname(__file__), '../')
sys.path.insert(0, folder_path)

import config

# Start.
from openai import AzureOpenAI

# TODO: Initialize Azure OpenAI client
client = ___

# TODO: Get the deployment name from the environment variable.
deployment = ___


# Helper function to call the model
def ask_llm(prompt: str):
    """Send a prompt to Azure OpenAI and return response text"""
    print(f"\n ask_llm()...")

    # TODO: call the Azure OpenAI client to get a response for the prompt.
    # Use the client.chat.completions.create() method.
    # Provide values for model, messages and temperature parameters.
    # Keep the temperature a bit higher (0.7) to see variations in the output.
    # Message must define the role as "user" and pass the prompt as content.
    response = ___

    return response.choices[0].message.content


# TODO: Define a Poor prompt (ambiguous, no structure)
poor_prompt = "___"

# TODO: Define an Improved prompt (clear role + context + structure)
better_prompt = """
___
"""


# TODO: call the llm with the poor prompt and print the output.
___

# TODO: call the llm with the refined better prompt and print the output.
___
