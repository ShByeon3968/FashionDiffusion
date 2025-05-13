from PIL import Image
import os

input_dir = "hanbok"
output_dir = "hanbok_resized"
os.makedirs(output_dir, exist_ok=True)

for fname in os.listdir(input_dir):
    img = Image.open(os.path.join(input_dir, fname)).convert("RGB")
    img = img.resize((1024, 1024))
    img.save(os.path.join(output_dir, fname))