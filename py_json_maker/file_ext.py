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
        
        working_status = f"working on >> {file_path}, \n"
        print(working_status)

        # extract text from pdf file
        text_content = get_pdf_texts(file_path)

        # write text content to json file
        
        append_Json(dir_path, text_content)

        append_Json_status = f">> DONE  - write {file_path} to json file \n"
        print(append_Json_status)

    elif file_extension == ".txt":
        print(file_extension)


if __name__ == "__main__":
    check_file_ext(file_name)
