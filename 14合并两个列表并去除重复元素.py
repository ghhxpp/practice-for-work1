import random
alist = ['a','b','c','d','e','f']
blist = ['x','y','z','d','e','f']
def merge(*args):
    print(args)
    s = set()
    for a in args:
        s = s.union(a)
    return sorted(list(s))
print(merge(alist,blist))


