import openai
import os
import json

def Text(input):
	#TODO add querying prompt for video generation

	openai.api_type = "azure"
	openai.api_base = os.getenv("OPENAI_API_BASE")
	openai.api_version = "2023-05-15"
	openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")

	conversation = [
	{"role": "system", "content": "You are a director and screenwriter. You writes video scripts and prompt for video generation."},
	{"role": "user", "content": "based on the text provided, Generate a set of: 1. scripts, and 2. prompts for image/video generation of several scene that can be combined into a interesting story, each prompt wil be describing the coresponding scene."},
	{"role": "user", "content": "A dog running in the beach."},
	{"role": "assistant", "content": '''Scripts:
1. A black Labrador runs out from a house towards the beach.
2. The dog reaches the beach and starts running along the shoreline.
3. The dog jumps into the water and starts swimming playfully.
4. A group of children playing on the beach notice the dog and start playing with him.
5. The dog runs with the children along the beach, playing fetch and leaping through the waves.
6. As the sun sets and the sky turns orange, the dog lays down next to the children, panting happily.

Prompts:
1. Capture the dog's excitement as he leaves the house and runs towards the beach.
2. Highlight the beauty of the ocean as the dog runs along the shoreline.
3. Get low to the ground to capture the dog splashing through the water.
4. Film the children's reactions to the dog as they play with him.
5. Capture the dog's playful spirit as he runs with the children and jumps through the waves.
6. Show the beauty of the sunset as the dog and the children lay on the beach together.'''}
]

	conversation.append({"role": "user", "content": input})

	response = openai.ChatCompletion.create(
		engine="gpt-35-turbo", # The deployment name you chose when you deployed the ChatGPT or GPT-4 model.
		messages = conversation
	)

	ans = response['choices'][0]['message']['content']

	return ans