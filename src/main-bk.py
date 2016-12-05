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

def main(config_file_list):
    content_list = []
    for i in config_file_list:
        content_list.append(read_json_file(i))
    while 1:
        time.sleep(0.5)
        for i in content_list:
            main_loop(i['config'])


if __name__ == "__main__":
    print "SIS ( software interlock system ) begins ..."
#    config_file_list = ["../config/sncCorrectorlock.json", "../config/vacuum_interlock_config.json"]
    config_file_list = ["../config/demo.json" ]
    print config_file_list
    main(config_file_list)
