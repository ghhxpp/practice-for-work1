# -*- coding:utf-8 -*-

def jiecheng(n):
    if n == 1:
        return 1
    return jiecheng(n-1)*n
print(jiecheng(6))

def jiecheng2(n):
    s = 1
    for i in range(1,n+1):
        s = s*i
    return s
print(jiecheng(6))
