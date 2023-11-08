#!/usr/bin/python3

import os

from sentence_tokenizer import tokenize_sentence

# get pdf file
def fetch_pdf_file(pdf_file_directory):
    _, file_extension = os.path.splitext(pdf_file_directory)
    if file_extension == ".pdf" or file_extension == ".Pdf":
        return pdf_file_directory
    else:
        return not_pdf_file()


# its not a pdf file

def not_pdf_file():
    return "It is not a Pdf file!\n Needs a valid pdf file!"



if __name__ == "__main__":
    fetch_pdf_file(file_name)
