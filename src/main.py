#!/usr/bin/python
# -*- coding:utf-8 -*-

# ******************************************************
# Author       : Yifan Song
# Last modified: 2016.12.29
# Email        : yifans@mail.ustc.edu.cn
# Filename     : main.py
# Description  : SIS main
# ******************************************************

from core import sis_core
from log import sis_logger
import logging


def main():
    core = sis_core.SISCore("/home/yifans/code/PycharmProjects/HLS-II-SIS/config")
    core.process()

if __name__ == "__main__":
    sis_logger.set_sis_logger()
    logger = logging.getLogger("SIS_logger")
    logger.info("SIS ( software interlock system ) begins ...")
    main()

