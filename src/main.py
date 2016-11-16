#!/usr/bin/python

import json
import time
from epics import PV

import interlock_unit
from read_json import read_json_file


def main_loop(config_information):
    for i in config_information:
        interlock_unit_config = i['interlock_unit']
        interlock_unit_i = interlock_unit.InterlockUnit(interlock_unit_config)
        interlock_unit_i.process_interlock()

def main():
    content = read_json_file('./config/vacuum_interlock_config.json')
    while 1:
        time.sleep(0.5)
        main_loop(content['config'])

if __name__ == "__main__":
    print "SIS ( software interlock system ) begins ..."
    main()