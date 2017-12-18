#!/usr/bin/env python
#coding=utf-8

import struct

def mypack(data):
    pack_format = '2I%ds'
    return struct.pack(pack_format % len(data),100,len(data),data)

#简单解码
def myunpack(data):
    pack_format = '2I%ds' % (len(data) - 2*4)
    return struct.unpack(pack_format,data)

#解码+处理粘包
def myunpack2(data):
    pack_format = '2I%ds' % (len(data) - 2*4)
    (version,length,str) = struct.unpack(pack_format,data)

    if 0 < ((len(data) - 2*4)-length):
        #如果有粘包，则将后续字段，放入一个字符串中
        pack_format = '2I%ds%ds' % (length, (len(data) - 2*4)-length)
        return struct.unpack(pack_format,data)
    else:
        return (version,length,str)

 #测试
if __name__ == '__main__':

    import json
    str = {'a':1111,'b':[],'c':'asfasdf'}
    str = json.dumps(str)

    a = mypack(str)
    print a
    b = myunpack2(a+a+a)
    print b
    while 3<len(b):
        b = myunpack2(b[3])
        print b

