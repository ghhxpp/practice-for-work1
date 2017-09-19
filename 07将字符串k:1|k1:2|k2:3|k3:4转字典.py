# -*- coding:utf-8 -*-

# 将字符串："k:1|k1:2|k2:3|k3:4"，处理成 python 字典：{k:1, k1:2, ... }

a = "k:1|k1:2|k2:3|k3:4"
a = a.replace(":","=")
a = a.replace("|",",")
a = eval("dict(%s)" %a)
print(a)
