#!/usr/bin/python

import json
import time

from epics import caget

from read_json import read_json_file

class DeviceNode(object):
    def __init__(self, device_dict):
        self.status = False
        self.mask = device_dict["mask"]
        self.pv_name = device_dict["pv_name"]
        self.operator = device_dict["operator"]
        self.threshold = device_dict["threshold"]

    def getStatus(self):
        if self.mask == 0:
            return False
        else:
            self.refreshStatus()
            return self.status

    def refreshStatus(self):
        self.status = False
        pv_value_now = caget(self.pv_name)
        if self.operator == '>=':
            self.status = pv_value_now >= self.threshold
        elif self.operator == '<=':
            self.status = pv_value_now <= self.threshold
        elif self.operator == '==':
            self.status = abs(pv_value_now - self.threshold) <= 1e-12
        elif self.operator == '!=':
            self.status = abs(pv_value_now - self.threshold) > 1e-12
        else:
            print "operator " + self.operator + " is not support, please use >=, <=, ==, !="


if __name__ == "__main__":
    device_dict_demo = {
                  "type":"device_node",
                  "mask":1,
                  "pv_name":"PV_IN_1",
                  "operator":"and",
                  "threshold":-0.499
               }
    d = DeviceNode(device_dict_demo)
    print d.getStatus()
    #print type(d)
    #print device_dict_demo
