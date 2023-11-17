#!/usr/bin/python3

import os
from access_pdf_file import get_pdf_texts
from json_writer import json_writer


def check_file_ext(dir_path, file_path, total_files, file_number):
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
        json_writer(dir_path, text_content)

        if file_number < total_files - 1:
            json_writer(dir_path, ",")

        write_Json_status = f">> DONE  - write {file_path} to json file \n"
        print(write_Json_status)

    elif file_extension == ".txt":
        print(file_extension)


if __name__ == "__main__":
    check_file_ext(dir_path, file_path, total_files)
