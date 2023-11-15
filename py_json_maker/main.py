#!/usr/bin/python3

from pathlib import Path

from file_ext import check_file_ext


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
    parser.add_argument("-d", "--directory",
                         help="Enter file directory!")

    parser.add_argument("-f", "--file", 
                        help="Enter file path")
    
    parser.add_argument("-c", "--cwd",
                         help="current working directory")
    
    args = parser.parse_args()
    dir_path = args.file_directory

    # cmd args accept file, directory or no input
    # hence get cwd

    if dir_path:
        for file in Path(dir_path).rglob('*'):
            # check_file_ext(file)
            print(file)


    # TODO get the current working directory
    #  if no file path is provided
    #  ie. no args were provided 

    current_working_directory = Path.cwd()
    for file in Path(current_working_directory).rglob('*'):
        check_file_ext(file)


