#!/usr/bin/python
# -*- coding:utf-8 -*-

# ******************************************************
# Author       : Yifan Song
# Last modified: 2016.12.29
# Email        : yifans@mail.ustc.edu.cn
# Filename     : sis_core.py
# Description  : SIS core program
# ******************************************************
import logging
import sys

sys.path.append("..")

# from util import read_json
# from log import sis_logger

class SISCore(object):
    def __init__(self, config_file_path):
        #interlock_config = read_json.readjson(config_file_path)
        #print interlock_config
        pass

    def process(self):
        logger = logging.getLogger("SIS_logger")
        logger.info("SIS Core is processing")
