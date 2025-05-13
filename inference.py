from diffusers import StableDiffusionXLPipeline
import torch

# SDXL 기본 모델 로드
pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16,
).to("cuda")

# LoRA 병합
pipe.load_lora_weights("./hanbok-sdxl-lora")

# 추론
prompt = "photo of a hanbok outfit,upper body,beautiful, elegant fabric"
image = pipe(prompt, num_inference_steps=30, guidance_scale=7.0).images[0]

image.save("hanbok_sdxl_result.png")