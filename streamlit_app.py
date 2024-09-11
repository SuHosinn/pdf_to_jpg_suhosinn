from pdf2image import convert_from_path
from PIL import Image
import os

def pdf_to_jpg(pdf_path, output_folder):
    # PDF 파일을 이미지로 변환
    pages = convert_from_path(pdf_path, dpi=300)

    # 출력 폴더가 존재하지 않으면 생성
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 각 페이지를 JPG 파일로 저장
    for i, page in enumerate(pages):
        output_path = os.path.join(output_folder, f"page_{i+1}.jpg")
        page.save(output_path, 'JPEG')
        print(f"Saved {output_path}")

# 사용 예
pdf_path = 'example.pdf'  # 변환할 PDF 파일 경로
output_folder = 'output_images'  # JPG 파일을 저장할 폴더 경로
pdf_to_jpg(pdf_path, output_folder)
