import argparse, sys
import json

import mixVideo
import text
import voice
import text2video


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
	ans = text.Text(input)
	try:
		generated_text = json.loads(ans)
		print("GPT response: ")
	except:
		print("Error: Can't parse GPT response.")
		print("Using example text.")
		generated_text = {"Scripts": ["A black Labrador runs out from a house towards the beach."], "Prompts": ["A black Labrador runs out from a house towards the beach."]}

	script = generated_text['Scripts'][0]
	print('Script: ' + script)

	prompt = generated_text['Prompts'][0]
	print('Prompt: ' + prompt)

	generated_voice = voice.Voice(script)
	video = text2video.text2video(prompt, fps=4, dry_run=dry_run)

	videoName =  str(abs(hash(script + prompt))) + ".mp4"

	outputPath = "./Web/videos/" + videoName
	mixVideo.merge_video_audio(video, generated_voice, outputPath)
	print(videoName)

if __name__ == '__main__':
	main()