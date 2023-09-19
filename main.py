import argparse, sys
import json
import os
from concurrent.futures import ThreadPoolExecutor

import mixVideo
import text
import voice
from text2video import Generator
from moviepy.editor import *

generator = Generator()
def generate_clip(prompt, script, dry_run=False):
	generated_voice = voice.Voice(script)
	generated_video = generator.text2video(prompt, fps=4, dry_run=dry_run)

	videoName = str(abs(hash(script + prompt))) + ".mp4"

	outputPath = "./Web/videos/" + videoName

	mixVideo.merge_video_audio(generated_video, generated_voice, outputPath)

	return outputPath

def main():
	parser=argparse.ArgumentParser()

	dry_run = False

	parser.add_argument("--dry-run", help="use example video", action="store_true")
	parser.add_argument("prompt", help="prompt to generate video from",nargs='+')
	args = parser.parse_args()

	if args.dry_run: dry_run = False

	#combine args.prompt into one string
	args.prompt = ' '.join(args.prompt)

	input = args.prompt

	print("Generating prompts & scripts.")

	ans = text.Text(input)

	text_file_name = str(abs(hash(ans))) + ".json"
	text_file_dir = "media/texts/"
	text_path = text_file_dir + text_file_name

	if not os.path.exists(text_file_dir):
		os.mkdir(text_file_dir)

	try:
		generated_texts = json.loads(ans)

	except:
		print("Error: Can't parse GPT response.")
		print("Using example text.")

		generated_texts = [{"script": "A black Labrador runs out from a house towards the beach.",
						"prompt": "A black Labrador runs out from a house towards the beach."}]

	with open(text_path, "w", encoding="utf-8") as text_file:
		json.dump(generated_texts, text_file, indent=4)

	# send text file name to node server
	print("Prompts & scripts saved to " + text_path + ".")

	clips = []

	executor = ThreadPoolExecutor(max_workers=3)

	if not os.path.exists("./Web/videos/"):
		os.mkdir("./Web/videos/")

	scripts = [generated_text['script'] for generated_text in generated_texts]
	prompts = [generated_text['prompt'] for generated_text in generated_texts]

	# generate clips in parallel
	futures = executor.map(generate_clip, prompts, scripts)
	executor.shutdown()

	results = list(futures)

	for clip_path in results:
		clip = VideoFileClip(clip_path)
		clips.append(clip)

	# 串接影片
	final_video = concatenate_videoclips(clips)

	final_video_path = "./Web/videos/target.mp4"
	# 生成目標影片
	final_video.to_videofile(final_video_path, fps=24, remove_temp=False)

if __name__ == '__main__':
	main()