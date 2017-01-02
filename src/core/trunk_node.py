#!/usr/bin/python
# -*- coding:utf-8 -*-

# ******************************************************
# Author       : Yifan Song
# Last modified: 2017,
# Email        : yifans@mail.ustc.edu.cn
# Filename     : leaf_node.py
# Description  : the truck node in the interlock tree
# ******************************************************

import logging
import leaf_node

class TrunkNode(object):
    def __init__(self, trunk_dict):
        self.mask = trunk_dict['mask']
        self.expression = trunk_dict['expression']
        self.child = []
        self.action = []
        self.status = False

    def get_status(self):
        if self.mask == 0:
            return False
        else:
            self.refresh_status()
            return self.status

    def refresh_status(self):
        self.status = False
        child_status_list = []
        for monitor in self.child:
            monitor_status = monitor.get_status()
            child_status_list.append(monitor_status)

        fault_sum = 0
        for i in child_status_list:
            if i == True:
                fault_sum += 1

        if self.expression == "or":
            if max(child_status_list) == True:
                self.status = True
        elif self.expression == "and" :
            if min(child_status_list) != False:
                self.status = True
        elif self.expression[:11] == "fault_count" and self.expression[11:13] == ">=":
            fault_num = int(self.expression[13:])
            if fault_sum >= fault_num:
                self.status = True
        elif self.expression[:11] == "fault_count" and self.expression[11:13] == "<=":
            fault_num = int(self.expression[13:])
            if fault_sum <= fault_num:
                self.status = True
        else:
            logger = logging.getLogger("SIS_logger")
            logger.error(self.expression + " is not supported. Please use 'and, or, >=, <='")

    def process(self):
        self.refresh_status()
        if self.status == True:
            for i in self.action:
                i.execute_action()
        for i in self.child:
            if isinstance(i, TrunkNode):
                i.process()