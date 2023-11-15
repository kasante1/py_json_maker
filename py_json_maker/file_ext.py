#!/usr/bin/python3

import os
from access_pdf_file import get_pdf_texts

# get file contents
def check_file_ext(file_path):
    _, file_extension = os.path.splitext(file_path)

    if file_extension == ".pdf" or file_extension == ".Pdf":
        text_content = get_pdf_texts(file_path)
        print(text_content)

    elif file_extension == ".txt":
        print(file_extension)


if __name__ == "__main__":
    check_file_ext(file_name)
