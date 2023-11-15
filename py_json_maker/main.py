#!/usr/bin/python3

import os
from pathlib import Path

from access_pdf_file import *
# from pypdf import PdfReader

import colorama
# init the colorama module
colorama.init()

GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW


if __name__ == "__main__":
    import argparse

    title = """
       >> JSON MAKER \n """
    
    print(f"{RESET} {title}")

    parser = argparse.ArgumentParser(
        description="extract file contents to make json file"
    )
    parser.add_argument("file_directory", help="Enter file directory!")

    args = parser.parse_args()
    dir_path = args.file_directory


    # TODO get the current working directory
    #  if no file path is provided
    #  ie. no args were provided 

    # current_working_directory = os.getcwd()

    for files in Path(dir_path).rglob('*'):
        print(files)
    # # get pdf file contents
    # is_pdf_file = check_pdf_file(file_path)


    # if is_pdf_file:
    #     reader = PdfReader(file_path)
    #     # show progress bar
        
    #     counter_number_of_pages = 0
    #     total_number_of_pages = len(reader.pages)


