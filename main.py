import argparse, sys

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


def main():
	parser=argparse.ArgumentParser()

	dry_run = False

	parser.add_argument("--dry-run", help="use example video", action="store_true")
	parser.add_argument("prompt", help="prompt to generate video from",nargs='+')
	args = parser.parse_args()

	if args.dry_run: dry_run = True

	#combine args.prompt into one string
	args.prompt = ' '.join(args.prompt)

	input = args.prompt

	print("Generating script.")
	generated_text = text.Text(input)
	script = getLine(generated_text, "Scripts", 0)
	prompt = getLine(generated_text, "Prompts", 0)

	generated_voice = voice.Voice(script)
	video = text2video.text2video(prompt, fps=4, dry_run=dry_run)

	videoName =  str(hash(script + prompt))

	outputPath = "./media/" + videoName + ".mp4"
	mixVideo.merge_video_audio(video, generated_voice, outputPath)
	print(outputPath)

if __name__ == '__main__':
	main()