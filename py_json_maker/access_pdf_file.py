#!/usr/bin/python3

from pypdf import PdfReader

def get_pdf_texts(file_path):
    reader = PdfReader(file_path)

    total_number_of_pages = len(reader.pages)

    for page in total_number_of_pages:
        text = reader.pages[page]
        print(text.extract_text())

if __name__ == "__main__":
    get_pdf_texts(file_path)