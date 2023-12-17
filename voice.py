import os
import azure.cognitiveservices.speech as speechsdk


# TODO add language selection
def Voice(text, styledegree):
    if styledegree == "":
        styledegree = 2
        print("styledegree: default")
    else:
        print("styledegree: ", styledegree)

    speech_config = speechsdk.SpeechConfig(
        subscription=os.environ.get("AZURE_SPEECH_KEY"), region="eastasia"
    )

    # speech_config.speech_synthesis_voice_name = 'zh-TW-HsiaoYuNeural'
    speech_config.speech_synthesis_voice_name = "zh-CN-YunxiNeural"

    # better audio quality. source: https://learn.microsoft.com/en-us/answers/questions/1153900/azure-text-to-speech-api-file-output-significantly
    speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Riff24Khz16BitMonoPcm)  

    # ssml
    ssml = f"""
		<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
            <voice name="zh-CN-YunxiNeural" style="cheerful" styledegree="{styledegree}">
				{text}
            </voice>
        </speak>
 		"""
    # Check if the directory exists
    if not os.path.exists("./media/voice"):
        # Create a new directory
        os.mkdir("./media/voice")

    filename = "./media/voice/" + text.replace(" ", "_")[:24] + str(hash(text)) + ".wav"

    audio_config = speechsdk.audio.AudioOutputConfig(filename=filename)

    speech_synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config
    )

    print("generating voice")

    # speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
    speech_synthesis_result = speech_synthesizer.speak_ssml_async(ssml).get()  # 改用ssml
    print("voice generated")

    if (
        speech_synthesis_result.reason
        == speechsdk.ResultReason.SynthesizingAudioCompleted
    ):
        print("Speech synthesized for text [{}]".format(text))
        return filename
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")
        return None
