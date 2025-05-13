import os
import json

def generate_metadata_jsonl(image_dir, output_path, default_prompt):
    image_extensions = {'.jpg', '.jpeg', '.png'}
    image_files = sorted([
        f for f in os.listdir(image_dir)
        if os.path.splitext(f)[-1].lower() in image_extensions
    ])

    with open(output_path, 'w', encoding='utf-8') as jsonl_file:
        for image_file in image_files:
            entry = {
                "file_name": image_file,
                "text": default_prompt
            }
            jsonl_file.write(json.dumps(entry, ensure_ascii=False) + '\n')

    print(f"[✓] metadata.jsonl 생성 완료: {output_path}")
    print(f"총 이미지 수: {len(image_files)}")

# 예시 사용법
if __name__ == "__main__":
    image_dir = "./hanbok_resized"  # 이미지가 들어있는 폴더 경로
    output_jsonl = "./hanbok_resized/metadata.jsonl"  # 생성할 jsonl 경로
    default_prompt = "photo of a hanbok outfit"  # 공통 prompt

    generate_metadata_jsonl(image_dir, output_jsonl, default_prompt)
