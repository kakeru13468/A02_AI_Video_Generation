import sys
import torch
import imageio
from diffusers import TextToVideoZeroPipeline
import tomesd
# from accelerate import Accelerator

# accelerator = Accelerator()
# device = accelerator.device

def text2video(prompt, fps=4, dry_run=False):
	model_id = "runwayml/stable-diffusion-v1-5"
	filename ='./media/' + prompt.replace(" ", "_")[:16] + '.mp4'
	
	if not dry_run:
		#if on mac
		if sys.platform == "darwin":
			device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
			pipe = TextToVideoZeroPipeline.from_pretrained(model_id).to(device)
			pipe.enable_attention_slicing() #for low memory usage
		else:
			device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
			pipe = TextToVideoZeroPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to(device)
			tomesd.apply_patch(pipe, ratio=0.5)

		result = pipe(prompt=prompt).images
		result = [(r * 255).astype("uint8") for r in result]
	
		imageio.mimsave(filename, result, fps=fps)
	else: filename = "media/example.mp4"

	return filename