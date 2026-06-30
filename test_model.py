import argparse
import os
from openai import OpenAI


endpoint = "https://cir-openai.services.ai.azure.com/openai/v1"

parser = argparse.ArgumentParser()
parser.add_argument("deployment_name", nargs="?", default="gpt-4.1-nano")
args = parser.parse_args()

client = OpenAI(
    base_url=endpoint,
    api_key=os.getenv("CIR_AZURE_API")
)

response = client.responses.create(
    model=args.deployment_name,
    input="What is the capital of France?",
)

print(f"answer: {response.output[0]}")
