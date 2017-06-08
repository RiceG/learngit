#! /usr/bin/python3

class Test:
    name = 'wg'

    def __init__(self, age):
        self.age = 18

    def p(self):
        print(Test.name)
        print(self.name)
        print(self.age)

    def set(self, n):
        self.name = n
        self.p()


def p():
    print(Test.name)
    print(a.name)

a =Test(20)
p()

Test.name = 'wan'
p()

a.p()

a.name = 'gu'
p()

Test.p(a)
a.p()

a.set('hahah')
