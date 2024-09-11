import streamlit as st
import fitz  # PyMuPDF
import io

def pdf_to_jpg(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    images = []
    for i in range(len(doc)):
        page = doc.load_page(i)
        pix = page.get_pixmap()
        img_buffer = io.BytesIO(pix.tobytes("jpeg"))
        img_buffer.seek(0)
        images.append((img_buffer, f"page_{i+1}.jpg"))
    return images

st.title("PDF to JPG Converter")

pdf_file = st.file_uploader("Upload PDF file", type=["pdf"])

if pdf_file:
    st.write("Converting PDF to JPG...")
    images = pdf_to_jpg(pdf_file)
    
    for img_buffer, filename in images:
        st.image(img_buffer, caption=filename)

        # 제공된 이미지 파일을 다운로드할 수 있는 버튼 추가
        st.download_button(
            label="Download " + filename,
            data=img_buffer,
            file_name=filename,
            mime="image/jpeg"
        )

    st.success("Conversion complete!")
