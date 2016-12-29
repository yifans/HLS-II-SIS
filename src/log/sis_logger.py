#!/usr/bin/python
# -*- coding:utf-8 -*-

# ******************************************************
# Author       : Yifan Song
# Last modified: 2016.12.29
# Email        : yifans@mail.ustc.edu.cn
# Filename     : sis_logger.py
# Description  : SIS Logger Module
# ******************************************************

import logging

def set_sis_logger():
    # 设置logging参数
    logger_name = "SIS_logger"  # 获取的Logger名称
    path = "/tmp/sis_log.log"  # 日志文件保持路径，缺省为在当前目录下的"./tmp/sis_log.log"
    l_level = logging.DEBUG  # 设置logging等级
    s_level = logging.DEBUG  # 向stream中输出日志的等级
    f_level = logging.DEBUG  # 向文件中输出日志的等级
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'  # 日志格式

    # 获取logger
    logger = logging.getLogger(logger_name)
    formatter = logging.Formatter(fmt)
    logger.setLevel(l_level)
    # 设置 Stream Handler
    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    sh.setLevel(s_level)
    # 设置 File Handler
    fh = logging.FileHandler(path)
    fh.setFormatter(formatter)
    fh.setLevel(f_level)
    # 添加进logger
    logger.addHandler(sh)
    logger.addHandler(fh)
