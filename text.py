import openai
import os
import json

def Text(input):

	openai.api_type = "azure"
	openai.api_base = os.getenv("OPENAI_API_BASE")
	openai.api_version = "2023-05-15"
	openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")

	conversation = [
	{"role": "system", "content": "You are a director and screenwriter. You writes video scripts and prompt for video generation."},
	{"role": "user", "content": "based on the text provided, Generate a set of: 1. scripts, and 2. prompts for image/video generation of several scene that can be combined into a interesting story, each prompt will be describing the corresponding scene."},
	{"role": "user", "content": "A dog running in the beach."},
	{"role": "assistant", "content": '''{"Scripts": ["A black Labrador runs out from a house towards the beach.",
"The dog reaches the beach and starts running along the shoreline.",
"The dog jumps into the water and starts swimming playfully.",
"A group of children playing on the beach notice the dog and start playing with him.",
"The dog runs with the children along the beach, playing fetch and leaping through the waves.",
"As the sun sets and the sky turns orange, the dog lays down next to the children, panting happily."],
"Prompts": ["A black Labrador runs out from a house towards the beach.",
"A black Labrador runs along the shoreline of the beautiful ocean.",
"A black Labrador jumps into the water and starts swimming playfully.",
"A group of children playing on the beach with the black Labrador.",
"A black Labrador runs with the children along the beach, playing fetch and leaping through the waves.",
"A black Labrador and the children lay on the beach together as the sun sets."]}'''}
]

	conversation.append({"role": "user", "content": input})

	response = openai.ChatCompletion.create(
		engine="gpt-35-turbo", # The deployment name you chose when you deployed the ChatGPT or GPT-4 model.
		messages = conversation
	)

	ans = response['choices'][0]['message']['content']

	return ans