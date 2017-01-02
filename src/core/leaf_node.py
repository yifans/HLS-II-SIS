#!/usr/bin/python
# -*- coding:utf-8 -*-

# ******************************************************
# Author       : Yifan Song
# Last modified: 2016.01.02
# Email        : yifans@mail.ustc.edu.cn
# Filename     : leaf_node.py
# Description  : the leaf node in the interlock tree
# ******************************************************

from epics import caget
import logging


class LeafNode(object):
    def __init__(self, leaf_dict):
        self.status = False
        self.mask = leaf_dict["mask"]
        self.pv_name = leaf_dict["pv_name"]
        self.compare_operator = leaf_dict["compare_operator"]
        self.design_value = leaf_dict["design_value"]

    def get_status(self):
        """
        返回当前leaf node 的状态，在返回之前，需要先刷新节点状态
        :return: 当前 leaf node 节点的状态
        """
        if self.mask == 0:
            return False
        else:
            self.refresh_status()
            return self.status

    def refresh_status(self):
        self.status = False
        pv_value_now = caget(self.pv_name)
        if self.compare_operator == '>=':
            self.status = pv_value_now >= self.design_value
        elif self.compare_operator == '<=':
            self.status = pv_value_now <= self.design_value
        elif self.compare_operator == '==':
            self.status = abs(pv_value_now - self.design_value) <= 1e-12
        elif self.compare_operator == '!=':
            self.status = abs(pv_value_now - self.design_value) > 1e-12
        else:
            logger = logging.getLogger("SIS_logger")
            logger.error("compare_operator " + " is not support, please use >=, <=, ==, !=")


if __name__ == "__main__":
    pass
