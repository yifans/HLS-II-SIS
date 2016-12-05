#!/usr/bin/pythn
from epics import caget
import device_node

class SignalNode(object):
    def __init__(self, single_dict):
#        print "---!!! Debug !!! ---"
#        print single_dict
#        print '---!!! Debug !!! ---'
        self.mask = single_dict['mask']
        self.expression = single_dict['expression']
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
            #if isinstance(monitor, device_node.DeviceNode):
            #    monitor_value = caget(monitor.pv_name)
            #    print "monitor_name" + monitor.pv_name + ", monitor value is " + str(monitor_value)
            child_status_list.append(monitor_status)

        if self.expression == "or":
            if max(child_status_list) == True:
                self.status = True
        elif self.expression == "and" :
            if min(child_status_list) == False:
                self.status = True
        else:
            print self.expression + " is not supported."

    def process(self):
        status = self.get_status()
        if status == True:
            for i in self.action:
                i.execute_action()
