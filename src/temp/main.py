#!/usr/bin/python

import json
import time
from epics import PV
import interlock_list as interli
from read_json import read_json_file

def main_loop(interlock):
#    print interlock
    interlock.process_interlock()

def main(config_file):
    content_list = []
    config = read_json_file(config_file)
    interlock_list = interli.InterlockList(config)
    while 1:
        time.sleep(0.5)
        main_loop(interlock_list)


if __name__ == "__main__":
    print "SIS ( software interlock system ) begins ..."
    config_file_list = "../config/demo2.json"
    print config_file_list
    main(config_file_list)
