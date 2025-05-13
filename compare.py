from diffusers import StableDiffusionXLPipeline
import torch
from PIL import Image
import matplotlib.pyplot as plt

# 공통 프롬프트
prompt = "photo of a hanbok outfit,upper body,beautiful face, elegant fabric"

# 기본 SDXL 모델 (fine-tune 전)
pipe_base = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16
).to("cuda")
image_base = pipe_base(prompt, num_inference_steps=30, guidance_scale=7.5).images[0]

# Fine-tune된 LoRA 모델 적용
pipe_base.load_lora_weights("./hanbok-sdxl-lora")
image_lora = pipe_base(prompt, num_inference_steps=30, guidance_scale=7.5).images[0]

# 시각화
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
axs[0].imshow(image_base); axs[0].set_title("Before LoRA Fine-tuning"); axs[0].axis("off")
axs[1].imshow(image_lora); axs[1].set_title("After LoRA Fine-tuning"); axs[1].axis("off")
plt.tight_layout()
plt.savefig("comparison_sdxl.png")
plt.show()
