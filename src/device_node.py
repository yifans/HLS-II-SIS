#!/usr/bin/python

from epics import caget


class DeviceNode(object):
    def __init__(self, device_dict):
        self.status = False
        self.mask = device_dict["mask"]
        self.pv_name = device_dict["pv_name"]
        self.operator = device_dict["operator"]
        self.threshold = device_dict["threshold"]

    def get_status(self):
        if self.mask == 0:
            return False
        else:
            self.refresh_status()
            return self.status

    def refresh_status(self):
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
        "mask": 1,
        "type": "device_node",
        "pv_name": "PV_IN_1",
        "operator": "and",
        "threshold": -0.499
    }
    d = DeviceNode(device_dict_demo)
    print d.get_status
    # print type(d)
    # print device_dict_demo
