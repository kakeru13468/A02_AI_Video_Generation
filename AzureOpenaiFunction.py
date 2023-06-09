import os
import openai
import azure.cognitiveservices.speech as speechsdk

#TODO rename class name, function name, and parameter name
class create():
    def __init__(self):
        pass

    def Text(text):
        #TODO add querying prompt for video generation

        openai.api_type = "azure"
        openai.api_base = os.getenv("OPENAI_API_BASE")
        openai.api_version = "2023-03-15-preview"
        openai.api_key = os.getenv("AZURE_OPENAI_API_KEY")
        path = './transcription.txt'
        f = open(path, 'w', encoding='UTF-8')

        conversation=[{"role": "system", "content": "You are a director and screenwriter. You writes video scripts and prompt for video generation."}]
        conversation.append({"role": "user", "content": text + ", create a story using this text."})

        response = openai.ChatCompletion.create(
            engine="gpt-35-turbo", # The deployment name you chose when you deployed the ChatGPT or GPT-4 model.
            messages = conversation
        )

        ans = response['choices'][0]['message']['content']
        #conversation.append({"role": "assistant", "content": ans})
        print(ans, file=f)
        f.close()
        return ans

    def Voice(voice):
        speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('AZURE_SPEECH_KEY'), region='eastasia')
        speech_config.speech_synthesis_language = "en-US"
        speech_config.speech_synthesis_voice_name = 'zh-TW-HsiaoYuNeural'
        audio_config = speechsdk.audio.AudioOutputConfig(filename="./voice/voice.wav")

        speech_synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=speech_config, 
            audio_config=audio_config)

        speech_synthesizer.speak_text_async(voice).get()

        return("success")