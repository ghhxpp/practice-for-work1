# -*- coding:utf-8 -*-

# 输入某年某月某日，判断这一天是这一年的第几天？(可以用 python 标准库)
import datetime

def which_day():
    y = raw_input("年:")
    n = raw_input("月:")
    d = raw_input("日:")
    date = datetime.datetime(int(y),int(n),int(d))
    first_day = datetime.datetime(int(y),1,1)
    days = (date-first_day).days
    print(days)
which_day()    
