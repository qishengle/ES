#! /usr/bin/env python3
# -*- coding:utf-8 -*-
from io import StringIO
from io import BytesIO

f=StringIO()
f.write('hello')
f.write(' world!')
print(f.getvalue())

b=BytesIO()
#print(b.read())
b.write(b'\xe4\xb8\xad\xe6\x96\x87')
b.write('chinese'.encode('utf-8'))
print(b.read())
print(b.getvalue())
m=BytesIO(b.getvalue())
print(b.read())
print(m.read())
