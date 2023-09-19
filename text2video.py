import sys
import torch
import imageio
from diffusers import TextToVideoZeroPipeline
import tomesd

class Generator:
	def __init__(self):
		self.spare_devices = [0] * torch.cuda.device_count()


	def text2video(self, prompt, fps=4, dry_run=False):
		model_id = "runwayml/stable-diffusion-v1-5"
		filename ='./media/' + prompt.replace(" ", "_")[:16] + '.mp4'

		if dry_run: filename = "media/example.mp4"
		else:
			#if on mac
			if sys.platform == "darwin":
				device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
				pipe = TextToVideoZeroPipeline.from_pretrained(model_id).to(device)
				pipe.enable_attention_slicing() #for low memory usage
			else:
				spare_device = self.checkin_device()
				if spare_device == -1:
					print("No spare devices available")
					return "media/example.mp4"
				device = torch.device(spare_device if torch.cuda.is_available() else "cpu")
				print("Using device:", device)
				pipe = TextToVideoZeroPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to(device)
				tomesd.apply_patch(pipe, ratio=0.5)

			result = pipe(prompt=prompt).images
			self.checkout_device(device.index)
			result = [(r * 255).astype("uint8") for r in result]

			imageio.mimsave(filename, result, fps=fps)

		return filename

	def checkin_device(self):
		for i in range(len(self.spare_devices)):
			if self.spare_devices[i] == 0:
				device = torch.device(f"cuda:{i}")
				self.spare_devices[i] = 1
				break
			else:
				device = -1
		return device

	def checkout_device(self, device_index):
		self.spare_devices[device_index] = 0