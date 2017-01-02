#!/usr/bin/python
# -*- coding:utf-8 -*-

# ******************************************************
# Author       : Yifan Song
# Last modified: 2017.01.02
# Email        : yifans@mail.ustc.edu.cn
# Filename     : action_unit.py
# Description  : the action unit in the trunk node
# ******************************************************

import time
import logging

#import datetime

from epics import caget, caput


# from epics import caget, caput

class ActionUnit(object):
    def __init__(self, action_dict):
        self.mask = action_dict["mask"]
        self.action_type = action_dict["action_type"]
        if self.action_type == "set":
            self.pv_name = action_dict["pv_name"]
            self.set_point = action_dict["set_point"]
        elif self.action_type == "delay":
            self.delay_time = action_dict["delay_time"]

    def execute_action(self):
        if self.mask == 0:
            print "The mask value is 0, so this node is passed."
        elif self.action_type == "set":
            pv_value_now = caget(self.pv_name)
            if abs(pv_value_now - self.set_point) >= 1e-8:
                caput(self.pv_name, self.set_point)
                logger = logging.getLogger("SIS_logger")
                logger.info(self.pv_name + "'s value is changed to " + str(self.set_point))
        elif self.action_type == "delay":
            # print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # print "delay %fs" % float(self.delay_time)
            time.sleep(float(self.delay_time))
            # print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
