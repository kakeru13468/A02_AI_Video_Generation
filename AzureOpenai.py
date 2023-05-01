import os
import openai
import azure.cognitiveservices.speech as speechsdk

openai.api_type = "azure"
openai.api_version = "2023-03-15-preview"      # The version of the Azure OpenAI resource you created.
openai.api_base = os.getenv("OPENAI_API_BASE")  # Your Azure OpenAI resource's endpoint value .
openai.api_key = os.getenv("OPENAI_API_KEY")    # Your Azure OpenAI resource's key value.

speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region='eastasia')
speech_config.speech_synthesis_language = "en-US"
speech_config.speech_synthesis_voice_name = 'zh-TW-HsiaoYuNeural'

audio_config = speechsdk.audio.AudioOutputConfig(filename="./voice/voice.wav")

speech_synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config, 
    audio_config=audio_config)

path = './translation/transcription.txt'
f = open(path, 'w', encoding='UTF-8')

conversation=[{"role": "system", "content": "You are a helpful assistant."}]

while(True):    
    conversation.append({"role": "user", "content": input("User: ") + "Please use that to create a story, rephrase it as one sentence."})

    if "bye" in conversation[-1]['content'].lower():
        print("Chatbot: Bye")
        f.close()
        break
    
    response = openai.ChatCompletion.create(
        engine="gpt-35-turbo", # The deployment name you chose when you deployed the ChatGPT or GPT-4 model.
        messages = conversation
    )

    ans = response['choices'][0]['message']['content']
    conversation.append({"role": "assistant", "content": ans})
    print("Chatbot: ", ans, file=f)
    print("Chatbot: ", ans)
    
    speech_synthesizer.speak_text_async(ans).get()