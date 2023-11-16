#!/usr/bin/python3

# import ndjson

# # Writing items to a ndjson file
# with open('./posts.ndjson', 'a') as json_writer:
#     writer = ndjson.writer(json_writer, ensure_ascii=False)

#     for post in posts:
#         writer.writerow(post)


import jsonlines
from split_paths import split_paths
# from pathlib import Path

def append_Json(json_file, text_content):    
    """
    append file contents to json file
    """

    # get_json_file_name = split_path(json_file)

    # # json_file_name = Path.joinpath(json_file, get_json_file_name[-1],'.json')

    # json_file_name = json_file + get_json_file_name[-1] + '.json'

    with jsonlines.open(json_file, mode='a') as writer:
        writer.write(text_content)

if __name__ == "__main__":
    append_Json(json_file, text_content)