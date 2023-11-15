#!/usr/bin/python3

import os


# get pdf file
def check_pdf_file(pdf_file_directory):
    _, file_extension = os.path.splitext(pdf_file_directory)
    if file_extension == ".pdf" or file_extension == ".Pdf":
        return pdf_file_directory
    else:
        return not_pdf_file()


# its not a pdf file

def not_pdf_file():
    return False



if __name__ == "__main__":
    fetch_pdf_file(file_name)
