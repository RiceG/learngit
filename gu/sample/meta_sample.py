#! /usr/bin/python3
# encoding:utf-8

# 元类会自动将你通常传给‘type’的参数作为自己的参数传入
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''
    #  选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    print(attrs)
    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
    print(uppercase_attr)
    # 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)

class UpperAttrMetaclass(type):
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        print(upperattr_metaclass)
        # 复用type.__new__方法
        # 这就是基本的OOP编程，没什么魔法
        return type.__new__(upperattr_metaclass, future_class_name, future_class_parents, uppercase_attr)

class UpperAttrMetaclass2(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        print(UpperAttrMetaclass2)
        print(cls)
        print(name)
        print(bases)
        print(dct)
        return super(UpperAttrMetaclass2, cls).__new__(cls, name, bases, uppercase_attr)

class Foo(object,metaclass = UpperAttrMetaclass2):
    bar = 'bip'
    
if hasattr(Foo,'BAR'):
    print(Foo.BAR)
else:
    print('no BAR')

if hasattr(Foo,'bar'):
    print(Foo.bar)
else:
    print('no bar')

