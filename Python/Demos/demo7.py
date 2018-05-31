#!/usr/bin/python
# -*- coding=utf-8 -*-
def fib(m):
    n,a,b=0,0,1
    while n<m:
        yield (b)
        a,b=b,a+b
        n=n+1
    return 'done'
f=fib(5)
#print(next(f))
#print(next(f))
#print(next(f))
#print(next(f))
#print(next(f))
#print(next(f))
#print(next(f))

#for i in fib(6):
 #   print (i)
#while 1:
#    try:
#        print('f:',next(f))
#    except StopIteration as e:
#        print ('Except :',e.value)
#        break
def triagle():
    L=[1]
    while True:
        yield L
        L.append(0)
        L=[L[i-1]+L[i]for i in range(0,len(L))]
        #n -=1
n=0
for i in triagle():
    print (i)
    n+=1
    if n==10:
        break
