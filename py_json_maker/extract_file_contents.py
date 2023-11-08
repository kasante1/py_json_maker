#!/usr/bin/python3

from access_pdf_file import *
from pypdf import PdfReader

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
    parser.add_argument("pdf_file_path", help="Enter pdf file directory path!")

    args = parser.parse_args()
    pdf_file_path = args.pdf_file_path

    # get pdf file contents
    pdf_file_location = fetch_pdf_file(pdf_file_path)


    # show progress bar

    reader = PdfReader(pdf_file_location)
    counter_number_of_pages = 0
    total_number_of_pages = len(reader.pages)


   
if __name__ == '__main__':
    main()
