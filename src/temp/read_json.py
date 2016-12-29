#!/usr/bin/python

import json

def read_json_file(json_file_path):
    with open(json_file_path) as json_file:
        raw_content = [line.strip() for line in json_file]
        data = ' '.join(raw_content)

    content = json.loads(data)
    return content


if __name__ == '__main__':
    content = read_json_file('../config/demo.json')
    print content
