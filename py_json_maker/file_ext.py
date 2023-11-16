#!/usr/bin/python3

import os
from access_pdf_file import get_pdf_texts
from json_writer import append_Json


def check_file_ext(dir_path, file_path):
    """
    get file contents
    according to the file extension

    """

    _, file_extension = os.path.splitext(file_path)

    if file_extension == ".pdf" or file_extension == ".Pdf":

        # extract text from pdf file
        text_content = get_pdf_texts(file_path)

        # write text content to json file
        
        append_Json('/home/asante/Documents/sql/sql.json', text_content)

    elif file_extension == ".txt":
        print(file_extension)


if __name__ == "__main__":
    check_file_ext(file_name)
