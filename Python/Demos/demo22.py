#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from enum import Enum,unique

month=Enum('MonTh',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

for name,member in month.__members__.items():
#value属性则是自动赋给成员的int常量，默认从1开始计数。
    #print (name,'==>',member,',',member.value)
    pass

@unique
class Weekday(Enum):
    Sun=0   #Sun's value is 0
    Mon=1
    Tue=2
    Wed=3
    Tur=4
    Fri=5
    Sat=6
print (Weekday.Sun)
print(Weekday['Tue'])
print(Weekday['Tur'].value)

