import openai
import azure.cognitiveservices.speech as speechsdk

openai.api_key = "Your_api_key"
speech_config = speechsdk.SpeechConfig(
    subscription='Your_api_key',
    region='eastasia')


ans = ""
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
]
path = './translation/translation.txt'
f = open(path, 'w', encoding='UTF-8')
i = 0
while True:
    audio_config = speechsdk.audio.AudioOutputConfig(
        use_default_speaker=True, filename="./voice/file"+str(i)+".wav")
    # zh-TW-HsiaoYuNeural #en-US-AshleyNeural
    speech_config.speech_synthesis_voice_name = 'zh-TW-HsiaoYuNeural'
    speech_synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config)

    messages.append({"role": "user", "content": input("User: ")})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # gpt-3.5-turbo,text-davinci-003
        messages=messages,
        max_tokens=2048,
        temperature=0.9,
    )

    if "bye" in messages[-1]['content'].lower():
        print("Bot: Bye")
        f.close()
        break

    print("ChatBot: ", response['choices'][0]['message']['content'])
    print("ChatBot: ", response['choices'][0]['message']['content'], file=f)
    speech_synthesis_result = speech_synthesizer.speak_text_async(
        response['choices'][0]['message']['content']).get()
    i = i+1
    ans = response['choices'][0]['message']['content']

    messages.append({"role": "assistant", "content": ans})
