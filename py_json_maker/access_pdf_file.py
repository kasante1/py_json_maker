#!/usr/bin/python3

from pypdf import PdfReader

def get_pdf_texts(file_path):

    pdf_contents = { 'filename': file_path, 'contents' : {} }

    reader = PdfReader(file_path)

    total_number_of_pages = len(reader.pages)

    print(total_number_of_pages)

    for page in range(total_number_of_pages):
        text = reader.pages[page]
        #  print(text.extract_text())
        text_contents = text.extract_text()
        pdf_contents['contents'].update( { page : text_contents })


text_content_structure = '''

{
    filename: "a book",

    contents:{
        0 : "page contents",
        1 : "page_contents",
        2 : "page_contents",
        }
}

'''



if __name__ == "__main__":
    get_pdf_texts(file_path)