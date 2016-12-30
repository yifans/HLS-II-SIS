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

from util import read_json

class SISCore(object):
    """
    SIS 的核心部分
    """
    def __init__(self, config_file_path):
        """
        SIS Core 初始化函数
        :param config_file_path: JSON配置文件路径
        """
        interlock_config = read_json.read_json_file(config_file_path)

    def process(self):
        logger = logging.getLogger("SIS_logger")
        logger.info("SIS Core is processing")