# -*- coding:utf-8 -*-

import functools
"""经过 @log装饰的，装饰器的作用是接受一个被包裹的函数作为参数，对其进行加工，返回一个包裹函数，代码使用 @functools.wraps装饰将要返回的包裹函数wrapper，使得它的 __name__， __module__，和 __doc__ 属性与被装饰函数now完全相同，这样虽然最终调用的是经过装饰的now函数，但是某些属性还是得到维护。
如果在 @log的定义中不使用 @function.wraps装饰包裹函数，那么最终now.__name__ 将会变成'inner'，而now.__doc__ 也会丢失。
将 @wraps(f)注释掉，然后运行程序，控制台输出，
inner
None
"""
def log(func):
    @functools.wraps(func)
    def inner():
        """innerinner"""
#        print("call %s()"%func.__name__)
        print("call "+func.__name__+"()")
        func()
    return inner

@log
def now():
    """nownow"""
    print('2013-12-25')
now()
print(now.__name__,now.__doc__)
# 输出：
# call now()
# 2013-12-25
