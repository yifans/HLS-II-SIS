#!/usr/bin/python

import device_node
import action_node
import signal_node

def get_interlock_tree(config_content):
    interlock_tree = []

    for i in config_content:
        interlock_tree.append(config_parse(config_content[i]))
    return interlock_tree

def config_parse(config_content):
    if config_content["node_type"] == "signal_node":
        s_node = signal_node.SignalNode(config_content)
        for i in config_content["child"]:
            node = config_parse(i)
            s_node.child.append(node)
        if "action_list" in config_content:
            for i in config_content["action_list"]:
                node = config_parse(i)
                s_node.action.append(node)
        return s_node

    elif config_content['node_type'] == "device_node":
        d_node = device_node.DeviceNode(config_content)
        return d_node

    elif config_content['node_type'] == "action_node":
        a_node = action_node.ActionNode(config_content)
        return a_node

if __name__ == '__main__':
    content = {
   "demo":{
      "node_type":"signal_node",
      "mask" : 1,
      "expression":"and",
      "child":[
         {
            "node_type":"signal_node",
             "mask" : 1,
            "expression":"or",
            "child":[
               {
                  "node_type":"device_node",
                  "mask":1,
                  "pv_name":"PV_1",
                  "operator":">=",
                  "threshold":3
               },
               {
                  "node_type":"device_node",
                  "mask":1,
                  "pv_name":"PV_2",
                  "operator":">=",
                  "threshold":1
               }
            ]
         },
         {
            "node_type":"device_node",
            "mask" : 1,
            "pv_name":"PV_3",
            "operator":">=",
            "threshold":1
         },
         {
            "node_type":"device_node",
            "mask" : 1,
            "pv_name":"PV_4",
            "operator":">=",
            "threshold":4
         }
      ],
      "action_list" : [
         {
            "node_type" : "action_node",
            "mask" : 1,
            "action_type":"set",
            "pv_name" : "PV_OUT_1",
            "set_point" : 0
         },
         {
            "node_type" : "action_node",
            "mask" : 1,
            "action_type":"delay",
            "delay_time" : 1
         }
      ]
   }
}
    print content
    print type(content)

    a = get_interlock_tree(content)
    print a
    print "done"
