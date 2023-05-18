import openai
import os
import json

def Text(input):
	#TODO add querying prompt for video generation

	openai.api_type = "azure"
	openai.api_base = os.getenv("OPENAI_API_BASE")
	openai.api_version = "2023-05-15"
	openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")

	#read prompt from file
	with open('prompt.json', 'r') as f:
		conversation = json.load(f)

	conversation.append({"role": "user", "content": input})

	response = openai.ChatCompletion.create(
		engine="gpt-35-turbo", # The deployment name you chose when you deployed the ChatGPT or GPT-4 model.
		messages = conversation
	)


	ans = response['choices'][0]['message']['content']
	#conversation.append({"role": "assistant", "content": ans})

	# write to file
	with open('./script.txt', 'w', encoding='UTF-8') as f:
		print(ans, file=f)

	return ans