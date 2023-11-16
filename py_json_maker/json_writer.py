#!/usr/bin/python3

import jsonlines
from split_paths import split_paths
import os

def append_Json(json_file, text_content, split_path = split_paths):    
    """
    append file contents to json file
    """

    get_json_file_name = split_path(json_file)

    # json_file_name = Path.joinpath(json_file, get_json_file_name[-1],'.json')
    
    json_file_name = f"{get_json_file_name[-1]}.json"
    
    json_file_path = os.path.join(json_file, json_file_name)

    with jsonlines.open(json_file_path, mode='a') as writer:
        writer.write(text_content)
    

if __name__ == "__main__":
    append_Json(json_file, text_content)