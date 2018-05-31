#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import os
#print(os.uname(),'***')
#print(os.environ)
p=os.path.abspath('.')
print(os.path.join(p,'dir2'))
#print(os.mkdir('./dir1'))
#print(os.rmdir('./dir1'))
lst=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]!=('.py')]
print (lst)
