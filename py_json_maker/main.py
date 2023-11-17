#!/usr/bin/python3

from pathlib import Path
from file_ext import check_file_ext
from json_writer import json_writer



import colorama
# init the colorama module
colorama.init()

GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW


if __name__ == "__main__":
    import argparse

    title = """>> JSON MAKER \n"""
    
    print(f"{RESET} {title}")

    parser = argparse.ArgumentParser(
        description="extract file contents to make json file"
    )
    parser.add_argument("-d", "--directory",
                         help="Enter file directory!")

    parser.add_argument("-f", "--file", 
                        help="Enter file path")
    
    parser.add_argument("-c", "--cwd", action="store_true",
                         help="current working directory")
    
    parser.add_argument("-v","--version", action="version", version="0.1.0")

    args = parser.parse_args()
    dir_path = args.directory
    file_path = args.file
    cwd = args.cwd

    # TODO cmd args accept file, directory or no input
    # hence get cwd
    
    if dir_path and Path(dir_path).is_dir():

        # add opening [ to json file
        json_writer(dir_path, "[")

        total_files = sum(1 for _ in Path(dir_path).rglob("*")) - 1

        counter = 0
        for file_number, file in enumerate(Path(dir_path).rglob("*")):

            check_file_ext(dir_path, file, total_files, file_number)

            print("\r [ ^ ] Processed files ", counter, " / ", total_files, end="")

            counter += 1

        # add closing ] to json file
        json_writer(dir_path, "]")

    elif file_path and Path(file_path).is_file():
        print(file_path)
    
    # get cwd when no args provided
    elif cwd and Path(cwd).is_dir():
        current_working_directory = Path.cwd()
        for file in Path(current_working_directory).rglob("*"):
            check_file_ext(file)
    

