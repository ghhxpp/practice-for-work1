# -*- coding:utf-8 -*-

# 有二维的list对象alist，假定其中的所有元素都具有相同的长度，写一段程序根据元素的第二个元素排序

lists = [['cd','ab'],['ef','ac']]

def sort_lists(lst):
    lst.sort(key=lambda x:x[1],reverse=True)
    return lst
print(sort_lists(lists))

