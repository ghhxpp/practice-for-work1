# -*- coding:utf-8 -*-

# 方法1,实现__new__方法   
# 并在将一个类的实例绑定到类变量_instance上,   
# 如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回   
# 如果cls._instance不为None,直接返回cls._instance   

class Single(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            # orig = super(Single, cls)
            cls._instance = super(Single, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
class Myclass(Single):
    def __init__(self, new_name):
        self.name = new_name
    
m1 = Myclass("xiaoming")
print(m1.name,id(m1))
m2 = Myclass("xiaohong")
print(m2.name,id(m2))
print(m1.name,id(m1))






