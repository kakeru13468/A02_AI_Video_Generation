import os
import azure.cognitiveservices.speech as speechsdk

def Voice(voice):
	speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('AZURE_SPEECH_KEY'), region='eastasia')
	speech_config.speech_synthesis_language = "en-US"
	speech_config.speech_synthesis_voice_name = 'zh-TW-HsiaoYuNeural'
	audio_config = speechsdk.audio.AudioOutputConfig(filename="./voice/voice.wav")

	speech_synthesizer = speechsdk.SpeechSynthesizer(
		speech_config=speech_config, 
		audio_config=audio_config)

	speech_synthesizer.speak_text_async(voice).get()