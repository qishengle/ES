#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading

# 创建全局ThreadLocal对象:
local_users = threading.local()

def process_user():
    # 获取当前线程关联的student:
    u = local_users.user
    print('Hello, %s (in %s)' % (u, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_users.user = name
    process_user()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

