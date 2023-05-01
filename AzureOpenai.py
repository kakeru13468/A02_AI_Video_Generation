import openai
import os
import azure.cognitiveservices.speech as speechsdk

openai.api_type = "azure"
openai.api_base = os.getenv("OPENAI_API_BASE") 
openai.api_version = "2023-03-15-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('AZURE_SPEECH_KEY'), region='AZURE_SPEECH_REGION')
audio_config = speechsdk.audio.AudioOutputConfig(filename="./voice.wav")
# zh-TW-HsiaoYuNeural #en-US-AshleyNeural
# speech_config.speech_synthesis_voice_name = 'zh-TW-HsiaoYuNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config, audio_config=audio_config)

ans = ""
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
]
path = './transcription.txt'
f = open(path, 'w', encoding='UTF-8')

while True:

    #user input
    messages.append({"role": "user", "content": input("User: ")})

    if "bye" in messages[-1]['content'].lower():
        print("Bot: Bye")
        f.close()
        break

    #openai response
    response = openai.ChatCompletion.create(
        model="gpt-35-turbo",  # gpt-3.5-turbo,Azure setname
        messages=messages,
    )

    #extract answer from response
    ans = response['choices'][0]['message']['content']

    #output answer
    print("ChatBot: ", ans)

    #write answer to file
    print("ChatBot: ", ans, file=f)

    #add answer to messages
    messages.append({"role": "assistant", "content": ans})

    speech_synthesizer.speak_text_async(ans).get()