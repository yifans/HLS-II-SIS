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

class SISLogger(object):
    """SIS日志模块

        封装了 Python 标准库内的 logging 模块，对日志记录的配置可以在__init__()函数的开始部分中设置
    """
    def __init__(self, logger_name = "SIS_logger", path ="/tmp/sis_log.log",s_level = logging.DEBUG,f_level = logging.DEBUG):
        #设置logging参数
        logger_name = "SIS_logger" # 获取的Logger名称
        path = "/tmp/sis_log.log"  # 日志文件保持路径，缺省为在当前目录下的"./tmp/sis_log.log"
        l_level = logging.DEBUG    # 设置logging等级
        s_level = logging.DEBUG    # 向stream中输出日志的等级
        f_level = logging.DEBUG    # 向文件中输出日志的等级
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s' # 日志格式

        # 获取logger
        self.logger = logging.getLogger(logger_name)
        self.formatter = logging.Formatter(fmt)
        self.logger.setLevel(l_level)
        # 设置 Stream Handler
        sh = logging.StreamHandler()
        sh.setFormatter(self.formatter)
        sh.setLevel(s_level)
        # 设置 File Handler
        fh = logging.FileHandler(path)
        fh.setFormatter(self.formatter)
        fh.setLevel(f_level)
        # 添加进logger
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

if __name__ == "__main__":
    logger = SISLogger()
    logger.debug("a debug message")
