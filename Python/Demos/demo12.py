#! /usr/bin/env python3
# -*- coding:utf-8 -*-
def by_name(x):
    return str.upper(x[0])

def by_score(s):
    return s[1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
l1=sorted(L,key=by_name)
print (l1)
l2=sorted(L,key=by_score,reverse=True)
print (l2)

def count():
    fs = []
    for i in range(1, 4):
        def ff():
            return i*i
        def mm():
            return i*2
        fs.append(ff)
    return fs

f1, f2, f3 = count()
print (f1())
print (f2())
print (f3())
print (f1.__name__)
print ('----------')

def log(func):
    def wrapper(*args,**kw):
        print('before %s ' % func.__name__)
        res=func(*args,**kw)
        print ('after %s' % func.__name__)
        return res
    return wrapper

def logtext(text):
    def dec(func):
        def wrapper(*args,**kw):
            print('%s before %s ' % (text,func.__name__))
            res=func(*args,**kw)
            print ('this after %s' % func.__name__)
            return res
        return wrapper
    return dec

@logtext('hello')
@log
def now():
    print ('20170101')

now()
