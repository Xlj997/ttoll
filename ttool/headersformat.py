#!/usr/bin/python3
# -*- coding: utf-8 -*-

def headers_f(headers_str):
    headers = {}
    dd = headers_str.split('\n')
    dd = [i for i in dd if i != '']
    for i in dd:
        zz = i.split(': ')
        headers[zz[0]] = zz[-1]
    return headers
