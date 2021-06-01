#!/usr/bin/env python
# -*- coding:utf-8 -*-

from dbs.dal.Whiteip import White

White_res = White()


def whiteips():
    list_ip = []
    for ip in White_res.white_ip():
        list_ip.append(ip[0])
    return list_ip
