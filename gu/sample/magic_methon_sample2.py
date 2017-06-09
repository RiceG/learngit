class storage(dict):

    def __init__(self, name):
        self.name = name
        
    # __call__方法用于实例自身的调用
    #达到()调用的效果
    def __call__ (self, key):
        print('called.')
        print(self.__dict__)
        try:
            return self.__dict__[key]
        except KeyError as k:
            return None

s= storage('gg')
print(s.name)
print(s('name'))

