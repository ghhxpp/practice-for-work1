
lst = range(1,11)
lst1 = filter(lambda x:x>5, lst)
print(lst1)

lst2 = map(lambda x:x+10, lst)
print(lst2)

lst3 = reduce(lambda x,y:x+y, lst)
print(lst3)
