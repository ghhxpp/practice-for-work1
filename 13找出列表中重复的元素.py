# -*- coding:utf-8 -*-

# 有一个长度是101的数组，存在1~100的数字，有一个是重复的，拿重复的找出来

lists = range(1,101)
lists.insert(50,80)
tmp = []
[tmp.append(i) for i in lists if lists.count(i)==2]
print(list(set(tmp)))
