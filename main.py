import argparse, sys
import json
import os

import mixVideo
import text
import voice
import text2video


def main():
	parser=argparse.ArgumentParser()

	dry_run = False
	scriptPath = "./Web/static/script.json"
	promptPath = ".Web/static/prompt.json"
    
	parser.add_argument("--dry-run", help="use example video", action="store_true")
	parser.add_argument("prompt", help="prompt to generate video from",nargs='+')
	args = parser.parse_args()

	if args.dry_run: dry_run = False

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

	outputPathResult = []
            
	for i in range(5):
		script = generated_text['Scripts'][i]
		print(i, script)
		prompt = generated_text['Prompts'][i]
		print(i, prompt)

		with open(scriptPath, "w", encoding="utf-8") as scriptFile:
			json.dump(script, scriptFile, indent=4)
		with open(promptPath, "w", encoding="utf-8") as promptFile:
			json.dump(prompt, promptFile, indent=4)
		generated_voice = voice.Voice(script)
		video = text2video.text2video(prompt, fps=4, dry_run=dry_run)

		videoName = str(abs(hash(script + prompt))) + ".mp4"

		outputPath = "./Web/videos/" + videoName

		if not os.path.exists("./Web/videos/"):
			os.mkdir("./Web/videos/")

		mixVideo.merge_video_audio(video, generated_voice, outputPath)

		 # 載入影片
		video = VideoFileClip(outputPath)
		# 加入到陣列
		outputPathResult.append(video)
	
		print(videoName)

	# 串接影片
	final_clip = concatenate_videoclips(outputPathResult)

	final_video = "./Web/videos/target.mp4"
	# 生成目標影片
	final_clip.to_videofile(final_video, fps=24, remove_temp=False)

if __name__ == '__main__':
	main()