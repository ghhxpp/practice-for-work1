# -*- coding:utf-8 -*-

# 反转由单词和不定个数空格组成的字符串，要求单词中的字母顺序不变。如："I am   a      boy"反转成“boy      a   am I”。
import re

a = "I am   a          boy"
print("".join(re.split("(\s)",a)[::-1]))

