import os
import re

# 설정
image_folder = "hanbok_resized"  # 이미지가 저장된 경로
base_prompt = "photo of a hanbok outfit, full body, high quality"  # 공통 프롬프트

# 정제 함수: 파일명에서 키워드 추출
def extract_keywords(filename):
    name = os.path.splitext(filename)[0]  # 확장자 제거
    name = re.sub(r'[^a-zA-Z0-9_]', ' ', name)  # 특수문자 제거
    words = name.lower().split('_')  # 구분자 기준 나누기
    keywords = ' '.join([w for w in words if w not in ['hanbok', 'photo', 'image']])  # 의미 없는 단어 제거
    return keywords.strip()

# 생성 루프
for fname in os.listdir(image_folder):
    if fname.lower().endswith(".jpg"):
        txt_name = os.path.splitext(fname)[0] + ".txt"
        txt_path = os.path.join(image_folder, txt_name)

        # 키워드 추출 및 프롬프트 생성
        keyword_part = extract_keywords(fname)
        full_prompt = base_prompt
        if keyword_part:
            full_prompt += f", {keyword_part}"

        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(full_prompt)

        print(f"Created: {txt_path} → {full_prompt}")
