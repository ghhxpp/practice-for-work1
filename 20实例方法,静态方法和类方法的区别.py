# -*- coding:utf-8 -*-
# 实例方法只能实例调用,类方法和静态方法都能被实例和类调用

class Animal(object):
    name = "Animals"
    __name = "2222222"
    
    def __init__(self,new_jiaosheng):
        self.sheng = new_jiaosheng
        self.__sheng = "11111111111"

    def jiaosheng(self):
        print(self.sheng)
        # print(slef.name) # 错误
        # print(name) # 错误
        print(Animal.name)
        print(self.__sheng)
        print(Animal.__name)
    @classmethod
    def yanse(cls):
        print("huangse")
        # print(name)  # 错误
        print(Animal.name)
        print(cls.name)
        # print(cls.sheng) 不能访问实例属性
        print(cls.__name)
    @staticmethod
    def xingdong():
        print("pao")
        print(Animal.name)
        print(Animal.__name)
        # print(sheng)   不能访问实例属性

    def function():
        print("function")

dog = Animal("wangwang")
dog.jiaosheng()
Animal.yanse()
dog.yanse()
Animal.xingdong()
dog.xingdong()

Animal.jiaosheng(dog)

Animal.function() #python3中才能用       

# print(dog.__sheng) 不能访问私有属性
