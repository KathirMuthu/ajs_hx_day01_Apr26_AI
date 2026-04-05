# Zero-shot vs Few-shot.

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

# TODO: Initialize Azure OpenAI client
client = ___

# TODO: Get the deployment name from the environment variable.
deployment = ___


def ask_llm(messages):
    """Send structured messages to LLM"""
    print(f"\n ask_llm()...")

    # TODO: call the Azure OpenAI client to get a response for the messages.
    # Use the client.chat.completions.create() method.
    # Provide values for model, messages and temperature parameters.
    # Keep the temperature low (0.2) to keep the output stable for comparison.
    response = ___

    return response.choices[0].message.content


# TODO: Define an intentionally ambiguous input text.
input_text = "___"


# TODO: Define a Zero-shot prompt (no examples)
# Specify role "system" to provide context and instructions to the model.
# Specify the content for the system role to classify sentiment as positive, negative or neutral.
# Specify role "user" and provide the input_text as content.
zero_shot_messages = [
___
]


# 
# TODO: Define a Few-shot (with examples → teaches structure + logic) prompt
# Specify role "system" to provide context and instructions to the model.
# Specify the content for the system role to extract the sentiment and reason from the text in a specific format.
# Provide 2 examples with the role of "user" and "assistant" to show how the input and output should look like.
# Finally, provide the actual query with the role of "user" and the input_text as content.
few_shot_messages = [
___
]


print("\n--- Zero-shot Output ---\n")
print(ask_llm(zero_shot_messages))

print("\n--- Few-shot Output ---\n")
print(ask_llm(few_shot_messages))
