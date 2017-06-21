#!/usr/bin/env python
# -*- coding: utf-8 -*-
import struct
fmt = '<3s3sHH'
with open('test.gif', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
b = bytes(header)
file_type, version, width, height = struct.unpack(fmt, b)
print(file_type, version, width, height)
del img
del header


for codec in ['gbk', 'utf-8', 'utf-16']:
    print(codec, '你好'.encode(codec), sep='\t')

