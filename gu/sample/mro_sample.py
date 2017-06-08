#! /usr/bin/pyhton3
#coding:utf-8

import inspect

class A(object):
    pass

class B(object):
    pass

class C(A, B):
    pass

print(inspect.getmro(C))
print(C.__mro__)
print(C.mro())
