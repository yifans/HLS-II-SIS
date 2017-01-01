#!/usr/bin/python
# -*- coding:utf-8 -*-

# ******************************************************
# Author       : Yifan Song
# Last modified: 2016.12.29
# Email        : yifans@mail.ustc.edu.cn
# Filename     : main.py
# Description  : SIS main
# ******************************************************

import logging

from core import sis_core
from log import sis_logger
from util import read_json


def main():
    #初始化日志
    sis_logger.set_sis_logger("./log/sis_log.txt")
    #初始化Core
    core = sis_core.SISCore("./config/interlock_config.json")

    logger = logging.getLogger("SIS_logger")
    logger.info("SIS ( software interlock system ) begins ...")
    core.process()

if __name__ == "__main__":
    main()
