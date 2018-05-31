#!/usr/bin/python
# -*- coding=utf-8 -*-
def fac(n):
    return fac_iter(n,1)

def fac_iter(num,s):
    if num==1:
        return s
    return fac_iter(num-1, num*s)
#print (fac_iter(100,1))
#print (fac_iter(1000,1))
#n=int(input('Input N:'))
i=0
n=3
#list_a=list(range(n+1)
#list_a.pop(0)
#list_b=[]
#list_c=[])
def hanoi(n,a,b,c):
    nu=n
    if n==1:
        global i
        i+=1
 #       list_c.append(list_a.pop())
        print('step %d: %s ---> %s' %(i,a,c))
    else:
        hanoi(n-1,a,c,b)    #借助C N-1个移动到B
        hanoi(1,a,b,c)      #直接移动到C
        hanoi(n-1,b,a,c)   #借助A N-1个移动到C
hanoi(3,'a','b','c')
