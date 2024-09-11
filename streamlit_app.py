import streamlit as st
from pdf2image import convert_from_path
from PIL import Image
import io
import os

def pdf_to_jpg(pdf_file):
    # PDF 파일을 이미지로 변환
    pages = convert_from_path(pdf_file, dpi=300)
    images = []
    
    for i, page in enumerate(pages):
        # 이미지 버퍼에 저장
        img_buffer = io.BytesIO()
        page.save(img_buffer, format='JPEG')
        img_buffer.seek(0)
        images.append((img_buffer, f"page_{i+1}.jpg"))
    
    return images

# Streamlit 애플리케이션
st.title("PDF to JPG Converter")

# PDF 파일 업로드
pdf_file = st.file_uploader("Upload PDF file", type=["pdf"])

if pdf_file:
    st.writ
