#!/usr/bin/python
# -*- coding:utf-8 -*-

# ******************************************************
# Author       : Yifan Song
# Last modified: 2017.01.02
# Email        : yifans@mail.ustc.edu.cn
# Filename     : config_parse.py
# Description  : parse the configuration file, and return the interlock tree list
# ******************************************************

import leaf_node
import trunk_node
import action_unit


def get_interlock_tree_list(config_info):
    interlock_tree_list = []
    for i in config_info:
        interlock_tree = get_interlock_tree(config_info[i])
        interlock_tree_list.append(interlock_tree)
    return interlock_tree_list


def get_interlock_tree(tree_config_info):
    interlock_tree = config_parse(tree_config_info)
    return interlock_tree


def config_parse(config_content):
    if config_content["node_type"] == "trunk_node":
        t_node = trunk_node.TrunkNode(config_content)
        for i in config_content["child"]:
            node = config_parse(i)
            t_node.child.append(node)
        if "action_list" in config_content:
            for i in config_content["action_list"]:
                a_unit = action_unit.ActionUnit(i)
                t_node.action.append(a_unit)
        return t_node

    elif config_content['node_type'] == "leaf_node":
        l_node = leaf_node.LeafNode(config_content)
        return l_node
