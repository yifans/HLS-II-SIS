#!/usr/bin/python

import config_parse as cp

class InterlockList(object):
    def __init__(self, config_content):
        self.interlock_list = []
        for i in config_content:
            node = cp.config_parse(config_content[i])
            self.interlock_list.append(node)

    def process_interlock(self):
        for i in self.interlock_list:
            i.process()
