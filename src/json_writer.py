#!/usr/bin/python3

from split_paths import split_paths
import os
import json


def get_json_file_name(json_file, split_path = split_paths):
    """
    get json file name and path to create json file
    """

    get_json_file_name = split_path(json_file)

    # json_file_name = Path.joinpath(json_file, get_json_file_name[-1],'.json')
    
    json_file_name = f"{get_json_file_name[-1]}.json"
    
    json_file_path = os.path.join(json_file, json_file_name)

    return json_file_path


def json_writer(json_file, text_content, json_file_path = get_json_file_name):    
    """
    write contents to json file
    """

    json_file_name = json_file_path(json_file)

    json_structure = ["[", "]", ","]

    if text_content in json_structure:
        with open(json_file_name, 'a') as writer:
            writer.writelines(text_content)
    else:
        with open(json_file_name, 'a') as writer:
            json.dump(text_content, writer)


# json_format = """

# [
#     {
#     "filename" : "a book",
#     "contents" : {
#     "0": "page 0 contents here",
#     "1": "page 1 contents here"}
#     },

#     {
#     "filename" : "a second book",
#     "contents" : {
#     "0": "page 0 contents here",
#     "1": "page 1 contents here"}
#     }
# ]

# TODO
# 1. write [
# 2. add the dictionaries
# 3. add comma after the dictionary
# 4. write the closing ]
# 5. 


# """


if __name__ == "__main__":
    json_writer(json_file, text_content)