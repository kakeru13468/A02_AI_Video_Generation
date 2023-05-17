import torch
import torch.nn as nn
import imageio
import tomesd
from diffusers import TextToVideoZeroPipeline
from AzureOpenaiFunction import create
from MixVideo import mix
from moviepy.editor import *
    
# load stable diffusion model weights
model_id_1 = "runwayml/stable-diffusion-v1-5"
model_id_2 = "dreamlike-art/dreamlike-photoreal-2.0"


# create a TextToVideoZero pipeline 
pipe = TextToVideoZeroPipeline.from_pretrained(model_id_1, torch_dtype=torch.float16).to("cuda")
tomesd.apply_patch(pipe, ratio=0.5)

# define the text prompt
text = input("User: ")
prompt = create.Text(text)
print("Generated story sentence:", prompt)

voice = create.Voice(prompt)
print("Generated voice: success")

# generate the video using our pipeline
result = pipe(prompt=prompt).images
result = [(r * 255).astype("uint8") for r in result]

# save the resulting image
imageio.mimsave("./video/video2.mp4", result, fps=2)
#-------------------------error-------------------------


# get video and voice path, order final video path
#gnerated_voice = "/home/kakeru/ProjectTest/venv/voice/voice.wav"
#gnerated_video = "/home/kakeru/ProjectTest/venv/video/video2.mp4"

# Merge video and voice
#mix.merge_video_audio(gnerated_voice, gnerated_video)

