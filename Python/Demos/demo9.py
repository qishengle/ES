#! /usr/bin/env python3
# -*- coding=utf-8 -*-
from functools import reduce

def sum(a,b,f):
    return f(a)+f(b)
#print (sum(-11,-3,abs))

def f1(x,y):
    return x*10+y
def f2(x):
    return x*x

l1=map(f2,[1,2,3,4])
print (reduce(f1,list(l1)))
print (reduce(f1,[1,3,5,7,9]))
print('-----------------')
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,'8': 8, '9': 9}[s]
print(list(map(char2num,'123')))
print('123')
print('-----------------')
def normalize(name):
    #name=lower(name)
    #n=0
    name=name.lower()
    s=''
    for i,j in enumerate(name):
        if i==0:
            s=s+j.upper()
        else:
            #s=s+i.lower()
            s+=j
        #n+=1
    return s
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)  

def prod(l):
    def mul(x,y):
        return x*y
    return reduce(mul,l)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
print('-------------')
def str2float(s):
    def f1(x):
        l1={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
             '7': 7, '8': 8, '9': 9,'.':-1}
        return l1[x]
    l2=map(f1,s)
    point=0
    def f2(x,y):
        nonlocal point
        if y==-1:
            point=1
            return x 
        if point==0:
            return x*10+y
        else :
            point*=10
            return x+y/point
    return reduce(f2,l2)
print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))
print (str2float('123.45'))
