#!/usr/bin/python
# -*- coding=utf-8 -*-
from multiprocessing import Pool,Process,Queue
import time,os,random

def write(q):
    print('process to write:%s' % os.getpid())
    for value in ['A','B','C']:
        print('put %s to queue..' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read:%s' % os.getpid())
    while True:
        value=q.get()
        print('Get %s from queue.' % value)

if __name__=='__main__':
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))

    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
