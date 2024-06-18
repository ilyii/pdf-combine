import streamlit as st
from pypdf import PdfMerger
import io

# Function to combine PDFs
def combine_pdfs(pdf_files):
    merger = PdfMerger()
    
    for pdf in pdf_files:
        merger.append(pdf)
    
    combined_pdf = io.BytesIO()
    merger.write(combined_pdf)
    merger.close()
    combined_pdf.seek(0)
    
    return combined_pdf

if __name__ == "__main__":
    st.title("PDF Merger")

    st.write("Upload multiple PDF files to combine them into a single PDF file.")

    uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

    col1, col2 = st.columns([1, 1])
    with col1:   
        if st.button("Combine PDFs"):
            if uploaded_files:
                # Combine PDFs
                combined_pdf = combine_pdfs(uploaded_files)
                
                # Provide download link for the combined PDF
                with col2:
                    st.download_button(
                        label="Download Combined PDF",
                        data=combined_pdf,
                        file_name="combined.pdf",
                        mime="application/pdf"
                    )
            else:
                st.warning("Please upload at least two PDF files.")