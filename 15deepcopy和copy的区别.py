# -*- coding:utf-8 -*-

import copy

lst = [["a","b"],["c","d"],["e","f"],"g"]
list1 = lst
list1.append(1)
list1[0].append(11)
print(lst,id(lst))
print(list1,id(list1))
# 赋值指向同一个地址,修改的是同一个列表

lst = [["a","b"],["c","d"],["e","f"],"g"]
list2 = copy.copy(lst)
list2.append(2)
list2[0].append(22)
print(lst,id(lst),id(lst[1]))
print(list2,id(list2),id(list2[1]))
# 浅拷贝指向两个不同地址,两个不同的列表,但是列表中的列表地址相同

lst = [["a","b"],["c","d"],["e","f"],"g"]
list3 = copy.deepcopy(lst)
list3.append(3)
list3[0].append(33)
print(lst,id(lst),id(lst[1]))
print(list3,id(list3),id(list3[1]))
# 深拷贝指向两个不同地址,两个不同的列表,列表中的列表地址也不同相同

#总结: copy 仅拷贝对象本身，而不拷贝对象中引用的其它对象。
    #  deepcopy 除拷贝对象本身，而且拷贝对象中引用的其它对象。

