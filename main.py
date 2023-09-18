import argparse, sys
import json
import os

import mixVideo
import text
import voice
import text2video
from moviepy.editor import *

def main():
	parser=argparse.ArgumentParser()

	dry_run = False
	
	if not os.path.exists("./Web/static/"):
		os.mkdir("./Web/static/")

	parser.add_argument("--dry-run", help="use example video", action="store_true")
	parser.add_argument("prompt", help="prompt to generate video from",nargs='+')
	args = parser.parse_args()

	if args.dry_run: dry_run = False

	#combine args.prompt into one string
	args.prompt = ' '.join(args.prompt)

	input = args.prompt

	print("Generating script.")
	ans = text.Text(input)
	text_path = "./Web/static/text.json"
	try:
		generated_text = json.loads(ans)
		with open(text_path, "w", encoding="utf-8") as text_file:
			json.dump(generated_text, text_file, indent=4)

	except:
		print("Error: Can't parse GPT response.")
		print("Using example text.")
		generated_text = {"script": "A black Labrador runs out from a house towards the beach.",
						"prompt": "A black Labrador runs out from a house towards the beach."}

	clips = []

	for i in generated_text:
		script = i['script']
		print(script)
		prompt = i['prompt']
		print(prompt)

		generated_voice = voice.Voice(script)
		generated_video = text2video.text2video(prompt, fps=4, dry_run=dry_run)

		videoName = str(abs(hash(script + prompt))) + ".mp4"

		outputPath = "./Web/videos/" + videoName

		if not os.path.exists("./Web/videos/"):
			os.mkdir("./Web/videos/")

		mixVideo.merge_video_audio(generated_video, generated_voice, outputPath)

		 # 載入影片
		clip = VideoFileClip(outputPath)
		# 加入到陣列
		clips.append(clip)

	# 串接影片
	final_video = concatenate_videoclips(clips)

	final_video_path = "./Web/videos/target.mp4"
	# 生成目標影片
	final_video.to_videofile(final_video_path, fps=24, remove_temp=False)

if __name__ == '__main__':
	main()