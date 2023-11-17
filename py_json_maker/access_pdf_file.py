#!/usr/bin/python3

from pypdf import PdfReader
from text_utils import sanitize_texts
from progress.bar import Bar


def get_pdf_texts(file_path):
    
    """
    get text contents in pdf file

    """

    pdf_contents = { "filename": str(file_path), "contents" : {} }

    reader = PdfReader(file_path)

    total_number_of_pages = len(reader.pages)

    # TODO progress bar total_number_of_pages

    bar = Bar("extracting text...", max= total_number_of_pages)

    for page in range(total_number_of_pages):

        text = reader.pages[page]
        
        #  strip text of all punctuation marks
        #  ie only numbers and letters
        text_contents = sanitize_texts(text.extract_text())

        pdf_contents["contents"].update( { str(page) : text_contents })

        bar.next()
    
    return pdf_contents


if __name__ == "__main__":
    get_pdf_texts(file_path)