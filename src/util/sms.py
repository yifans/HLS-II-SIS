#!/usr/bin/python
# -*- coding:utf-8 -*-

# ******************************************************
# Author       : Yifan Song
# Last modified: 2017.01.01
# Email        : yifans@mail.ustc.edu.cn
# Filename     : sms.py
# Description  : send sms using post method
# ******************************************************

# !/usr/bin/python
# coding=utf8

import urllib

def send_sms(phone_list, message):
    """
    使用POST方法发送短信
    :param phone_list: 收信人列表，可以有多个收信人，需要传入一个序列
    :param message: 短信内容，目前只支持英文，中文接收到的短信为乱码
    """
    httpClient = None

    url = "http://210.5.158.31/hy/"

    uid = 
    auth = 
    phones = ",".join(phone_list)

    try:
        params_dict = {"uid": uid,
                       "auth": auth,
                       "mobile": phones,
                       "expid": "0",
                       "msg": message}
        params = urllib.urlencode(params_dict)

        f = urllib.urlopen(url, params)
        print f.read()

    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

if __name__ == "__main__":
    phone_list = [""]
    # phone_list = ["15256011677", "15256011677"]
    #message = "Test the software interlock system"
    #message = "The vacuum system has failed (level 1), and the beam is removed."
    #message = "The vacuum system has failed (level 2), and the vacuum valve is closed."
    message = "The vacuum system has failed (level 3), and the vacuum gauge is closed."
    send_sms(phone_list, message)
