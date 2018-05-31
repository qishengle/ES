#!/usr/bin/python
# -*- coding=utf-8 -*-
'''
nihoa
'''

'''alpha=['a','b','c']
print(alpha)
print (len(alpha))
alpha.append('d')
alpha.insert(-0,'e')
print (alpha)

t=('a',['b','d'],'c')
print(t[0],t[1])
#t[0]='aa'
t[1][0]='ee'
print(t[0],t[1])

age = input('input your age:')
age=int(age)
if age>=6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

L = ['Bart', 'Lisa', 'Adam']
for i in L:
    print('hello',i)
print()
for i in range(3):
    print ('hello',L[i])
print ()

n=0
while n<101:
    n=n+1
    if n%10!=0:
        continue
    else:
        print (n)
'''
t1=(1,2,3)
t2=set([1,1,2,3,3])
d={t1}
print (d)

