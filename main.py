import mixVideo
import text
import voice
import text2video


def getLine(text, type, line):
	script_start = text.index(type+':') + len(type+':')
	script_end = text.index('\n\n')
	if type == 'Prompts': script_end = -1
	paragraph = text[script_start:script_end].strip().split('\n')[line].split('. ', 1)[-1]
	return paragraph


if __name__ == '__main__':
	input = input("User: ")
	text = text.Text(input)
	script = getLine(text, "Scripts", 0)
	prompt = getLine(text, "Prompts", 0)
	
	voice = voice.Voice(script)
	video = text2video.text2video(prompt, fps=2,dry_run=False)

	mixVideo.merge_video_audio(video, voice, "./media/output.mp4")
