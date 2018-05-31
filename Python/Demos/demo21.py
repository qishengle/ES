#! /usr/bin/env python3
# -*-coding:utf-8 -*-
class Student(object):
    def get_score(self):
        return self.__score

    def set_score(self,value):
        if not isinstance(value,int):
           raise ValueError('score must be an integer!')
        if not 0<=value<=100:
           raise ValueError('score must be in 0~100! ') 
        self.__score=value
#s=Student()
#s.set_score(101)
#print(s.get_score())

class Screen(object):
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError('input must be int !')
        self.__width=value

    @property
    def hight(self):
        return self.__hight

    @hight.setter
    def hight(self,value):
        if not isinstance(value,int):
            raise ValueError('input must be int !')
        self.__hight=value

    @property
    def resolution(self):
        return self.__width*self.__hight

sc=Screen()
sc.width=1024
sc.hight=768
print(sc.resolution)
assert sc.resolution == 786432, '1024 * 768 = %d ?' % sc.resolution
