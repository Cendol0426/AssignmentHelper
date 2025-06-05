from PyPDF2 import PdfMerger
import streamlit as st
from io import BytesIO

st.title("PDF Merger")
uploaded_files = st.file_uploader("Upload PDF files to merge", type="pdf", accept_multiple_files=True)
file_name = st.text_input("Merged file name (without .pdf):")

if uploaded_files and st.button("Merge PDFs"):
    merger = PdfMerger()

    for pdf in uploaded_files:
        merger.append(pdf)

    merged_pdf = BytesIO()
    merger.write(merged_pdf)
    merger.close()
    merged_pdf.seek(0)

    st.success("PDFs merged successfully!")
    st.download_button(
        label="📥 Download Merged PDF",
        data=merged_pdf,
        file_name=f"{file_name}.pdf",
        mime="application/pdf"
    )
