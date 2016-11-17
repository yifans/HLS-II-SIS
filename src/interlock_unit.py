#!/usr/bin/python
import time
import datetime
from epics import PV
from epics import caget, caput

from read_json import read_json_file

class Monitor(object):
    def __init__(self, monitor_dict):
        self.name = monitor_dict['pv_name']
        self.operator = monitor_dict['operator']
        self.limit = monitor_dict['limit']

    def get_monitor_status(self):
        monitor_status = False
        pv_value_now = caget(self.name)
        if self.operator == '>=':
            monitor_status = pv_value_now >= self.limit
        elif self.operator == '<=':
            monitor_status = pv_value_now <= self.limit
        elif self.operator == '==':
            monitor_status = pv_value_now == self.limit
        elif self.operator == '!=':
            monitor_status = pv_value_now != self.limit
        else:
            print "operator is error"
        return monitor_status

class Action(object):
    def __init__(self, action_dict):
        self.action = action_dict['action']
        if action_dict['action'] == "put":
            self.name = action_dict['pv_name']
            self.target = action_dict['target']
        if action_dict['action'] == "delay":
            self.delay_time = action_dict['delay_time']

    def execute_action(self):
        if self.action == 'put':
            pv_val = caget(self.name)
            if pv_val != self.target:
                caput(self.name, self.target)
                print self.name + "'s value is changed to " + str(self.target)
        if self.action == 'delay':
            print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print "dely %fs"%float(self.delay_time)
            time.sleep(float(self.delay_time))
            print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class InterlockUnit(object):

    def __init__(self, interlock_unit_config):
        self.fault_number = -1
        self.monitor_list = []
        self.action_list = []
        if 'fault_number' in interlock_unit_config:
            self.fault_number = interlock_unit_config['fault_number']
        for i in interlock_unit_config['monitor_list']:
            monitor = Monitor(i)
            self.monitor_list.append(monitor)
        for i in interlock_unit_config['action_list']:
            action = Action(i)
            self.action_list.append(action)

    def get_interlock_status(self):
        interlock_status = False
        if self.fault_number != -1:
            sum = 0
            for i in self.monitor_list:
                status = i.get_monitor_status()
                sum += status
            if sum >= self.fault_number:
                #print 'sum == ' + str(sum)
                interlock_status = True
        return interlock_status

    def execute_interlock(self):
        for i in self.action_list:
            i.execute_action()

    def process_interlock(self):
        if self.get_interlock_status():
            self.execute_interlock()


if __name__ == '__main__':
    vacuum_interlock_config_content = read_json_file('vacuum_interlock_config.json')
    interlock_unit = InterlockUnit(vacuum_interlock_config_content['config'][0]['interlock_unit'])

    while True:
        interlock_unit.process_interlock()
        time.sleep(1)
