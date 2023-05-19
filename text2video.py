import torch
import imageio
from diffusers import TextToVideoZeroPipeline
import tomesd
from accelerate import Accelerator

accelerator = Accelerator()
device = accelerator.device

def text2video(prompt):
	model_id = "runwayml/stable-diffusion-v1-5"
	pipe = TextToVideoZeroPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to(device)
	tomesd.apply_patch(pipe, ratio=0.5)

	result = pipe(prompt=prompt).images
	result = [(r * 255).astype("uint8") for r in result]
	imageio.mimsave("video.mp4", result, fps=4)