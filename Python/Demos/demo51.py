#!/usr/bin/python
# -*- coding=utf-8 -*-
from multiprocessing import Pool,Process,Queue
import time,os,random

def long_time_pro(name):
    print('run task %s (%s)' % (name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('%s runs %2f seconds. ' % (name,end-start))

if __name__=='__main__':
    print('parent process %s ' % os.getpid())
    p=Pool(6)
    for i in range(7):
        p.apply_async(long_time_pro,args=(i,))
    print('waiting for all subprocesses done')
    p.close()
    p.join()
    print ('All subprocesses done')
