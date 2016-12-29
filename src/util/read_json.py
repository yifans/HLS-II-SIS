#!/usr/bin/python
# -*- coding:utf-8 -*-

# ******************************************************
# Author       : Yifan Song
# Last modified: 2016.12.29
# Email        : yifans@mail.ustc.edu.cn
# Filename     : read_json.py
# Description  : read the json file, and return the content as a dict
# ******************************************************

import json


def read_json_file(json_file_path):
    """
    read the json file, and return the content as a dict
    :param json_file_path: 要处理的json文件路径
    :return: 将JSON文件中的内容作为一个字典返回
    """
    with open(json_file_path) as json_file:
        raw_content = [line.strip() for line in json_file]
        data = ' '.join(raw_content)

    content = json.loads(data)
    return content


if __name__ == '__main__':
    info = read_json_file('../config/demo.json')
    print info
