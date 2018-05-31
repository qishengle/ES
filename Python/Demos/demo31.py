#! /usr/bin/env python3
# -*- coding:utf-8 -*-
with open('./demo1.py','r') as f:
    #print(f.read())
    for i in f.readlines():
        print(i.strip())
    print(f.readlines())
