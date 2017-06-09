#! /usr/bin/pyhton3
# -*- coding: utf-8 -*-

class A(object):
    def __init__(self, name):
        self.name = name

    def hi(self):
        print("func hi.")

    def __setattr__(self, *args, **kwargs):  
        print('set {0} : {1}'.format(args,kwargs))  
        return object.__setattr__(self, *args, **kwargs)
    
    def __delattr__(self, *args, **kwargs):  
        print('del {0} : {1}'.format(args,kwargs))
        return object.__delattr__(self, *args, **kwargs)  

    def __getattr__(self, item):
        print('get {0}.'.format(item))

    def __getattribute__(self, *args, **kwargs):  
        print('getattribute {0} : {1}'.format(args,kwargs))  
        return object.__getattribute__(self, *args, **kwargs)

a = A('gg')

print(a.name)
print(a.age)
print(getattr(a,'name'))
print(getattr(a,'age'))

a.hi()
getattr(a,'hi')()

a.name = 'gg smd'
print(a.name)

delattr(a,'name')
print(a.name)
