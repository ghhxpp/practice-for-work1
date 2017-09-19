# -*- coding:utf-8 -*-

#现有两个元组(('a'),('b')),(('c'),('d'))，请使用python中匿名函数生成列表[{'a':'c'},{'b':'d'}]

a = (('a'),('b'))
b = (('c'),('d'))
c = map(lambda x:{x[0]:x[1]},zip(a,b))
print(c)
