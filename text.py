import openai
import os
import json


def Text(input, engine="gpt-35-turbo"):
    openai.api_type = "azure"
    openai.api_version = "2023-05-15"

    if engine == "gpt-35-turbo":
        openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT_GPT4")
        openai.api_key = os.getenv("AZURE_OPENAI_KEY_GPT4")
    # elif engine == "kakeruGPT4":
    # 	openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT_GPT4")
    # 	openai.api_key = os.getenv("AZURE_OPENAI_KEY_GPT4")

    conversation = [
        {
            "role": "system",
            "content": "You are a director and prompt engineer. You write video scripts and prompt for video generation.",
        },
        {
            "role": "user",
            "content": "based on the text provided, Generate a set of: 1. scripts, and 2. prompts for image/video generation of several scene that can be combined into a interesting story, each prompt will be describing the corresponding scene.",
        },
        {"role": "user", "content": "follow the format of the example below:"},
    ]

    with open("example.json", "r") as file:
        example = json.dumps(json.load(file))

    conversation.append({"role": "user", "content": example})
    conversation.append({"role": "user", "content": input})

    response = openai.ChatCompletion.create(engine=engine, messages=conversation)

    ans = response["choices"][0]["message"]["content"]

    return ans
