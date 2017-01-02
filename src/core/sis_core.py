#!/usr/bin/python
# -*- coding:utf-8 -*-

# ******************************************************
# Author       : Yifan Song
# Last modified: 2016.12.29
# Email        : yifans@mail.ustc.edu.cn
# Filename     : sis_core.py
# Description  : SIS core program
# ******************************************************

import sys
sys.path.append("..")
import logging
import time

from util import read_json
import config_parse

class SISCore(object):
    """
    SIS 的核心部分
    """
    def __init__(self, config_file_path):
        """
        SIS Core 初始化函数
        :param config_file_path: JSON配置文件路径
        """
        interlock_config_dict = read_json.read_json_file(config_file_path)
        self.interlock_tree_list = config_parse.get_interlock_tree_list(interlock_config_dict)

    def process(self):
        logger = logging.getLogger("SIS_logger")
        logger.info("SIS Core is processing")
        while True:
            time.sleep(1)
            for i in self.interlock_tree_list:
                i.process()

