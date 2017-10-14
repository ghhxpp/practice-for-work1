# -*- coding:utf-8 -*-

# 如何匹配<html><title></title></html>得到<html>
import re
 
strs = "<html><title></title></html>"
result1 = re.match(r"<.*>", strs)
result2 = re.match(r"<.*?>", strs)
print(result1.group())
print(result2.group())
             
