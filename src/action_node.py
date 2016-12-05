#!/usr/bin/python
import time
import datetime
from epics import PV
from epics import caget, caput

class ActionNode(object):
    def __init__(self, action_dict):
        self.mask = action_dict["mask"]
        self.action = action_dict["action_type"]
        if self.action == "set":
            self.pv_name = action_dict["pv_name"]
            self.set_point = action_dict["set_point"]
        elif self.action == "delay":
            self.delay_time = action_dict["delay_time"]

    def execute_action(self):
        if self.mask == 0:
            print "The mask value is 0, so this node is passed."
        elif self.action == "set":
            pv_value_now = caget(self.pv_name)
            if abs(pv_value_now - self.set_point) >= 1e-8:
                caput(self.pv_name, self.set_point)
                print self.pv_name + "'s value is changed to " + str(self.set_point)
        elif self.action == "delay":
            print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print "delay %fs"%float(self.delay_time)
            time.sleep(float(self.delay_time))
            print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    action_demo_dict_1 = {
            "node_type" : "action_node",
            "mask" : 0,
            "action_type":"set",
            "pv_name" : "PV_OUT_1",
            "set_point" : 2
         }
    action_demo_dict_2 = {
            "node_type" : "action_node",
            "mask" : 1,
            "action_type":"delay",
            "delay_time" : 1
         }

    a = ActionNode(action_demo_dict_2)
    b = ActionNode(action_demo_dict_1)
    a.execute_action()
    b.execute_action()
