#!/usr/bin/python3
from pathlib import Path
from sys import platform


def check_os():
    """
    check the operating system
    of the runtime env.
    """
    if platform == "linux" or platform == "linux2":
        return ("linux", "/")
    
    if platform == "darwin":
        return ("darwin", "/")
    
    if platform == "win32":
        return ("windows", "\\")


def split_paths(path, get_delimiter = check_os()):
    """
    split paths [unix and windows] according
    to delimiter [/, \\]
    """
    args_path = Path(path)

    if args_path.is_file() or args_path.is_dir():
        parent_path = args_path.parent
        _, delimiter = get_delimiter

        spilt_path = str(parent_path).split(delimiter)

        return spilt_path

    else:
        return None

if __name__ == "__main__":
    split_paths(text)