#!/usr/bin/python
# -*- coding=utf-8 -*-
def regit(count,name,gender='men'):
    print(count,name,gender)
#regit(12,'qq')
#print ('------------')
#regit(123,'aa','woman')
#def cal(*number):
#    s=0
#    for i in number:
#        s=s+i*i
#    return s
#print (cal(5,6,7))
#
#def city(name,loc,**k):
#    print ('Name-',name,'Loc-',loc,'Other-',k)
#names={'bj':1,'sh':2,'zz':'zhengzhou'}
#city('dalas','beijing',**names)
def f1 (a,b,c=0,*ar,**kw):
    print('a=',a,'b=',b,'c=',c,'*ar=',ar,'**kw=',kw)
def f2(a,b,c=0,*,s,**kw):
    print('a=',a,'b=',b,'c=',c,'s=',s,'**kw=',kw)

f1(1,2)
f1(1,2,3)
f1(1,2,3,'q',mm=22)
f2(1,2,s=3)
f2(1,2,s=5,rr='weqr')
print ('________')
ar=(7,8,9,1)
kw={'s':'ss'}
f1(*ar,**kw)
f2(*ar,**kw)

