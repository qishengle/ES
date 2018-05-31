#!/usr/bin/python
# -*- coding=utf-8 -*-
from collections import Iterable
import os
L=["aa","cc",'bb']
for i,va in enumerate(L):
    print (i,va)
print (isinstance(L,Iterable))
print ('--------------')
for i in [x*x for x in range(1,11) if x*x%2!=0]:
   print (i)
#for j in [m+n+z for m in 'abc' for n in 'def' for z in 'ghi']:
#    print (j)
for f in  [d for d in os.listdir('.')]:
    print (f)
print ('--------------')
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for i in [k.upper()+'='+v.lower() for k,v in d.items()]:
    print (i)
print (isinstance('asd',str))
print (isinstance(12,str))

L1 = ['Hello', 'World', 18, 'Apple', None,'']
L2=[i for i in L1 if isinstance(i,str)]
print ('L1',L1)
print ('L2',L2)
