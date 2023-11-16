#!/usr/bin/python3

import ndjson

# Writing items to a ndjson file
with open('./posts.ndjson', 'a') as json_writer:
    writer = ndjson.writer(json_writer, ensure_ascii=False)

    for post in posts:
        writer.writerow(post)


import jsonlines

with jsonlines.open('output.jsonl', mode='a') as writer:
    writer.write(...)