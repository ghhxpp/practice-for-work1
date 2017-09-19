# coding:utf-8 

import random

def t_to_o(t,o):
    office = []
    for i in range(o):
        office.append([])
    for i in range(1,t+1):
        random.choice(office).append(i)
    return office    

print(t_to_o(8, 3))

def t_to_o2():
    # office = [[]] * 3
    office = [[],[],[]]
    print(office)
    teachers = ['a','b','c','d','e','f','g','h']
    for teacher in teachers:
        index = random.randint(0,2)
        office[index].append(teacher)
    for i in range(len(office)):
        print("办公室%d的人数是:%d\n%s"%(i+1,len(office[i]),''.join(office[i])))
t_to_o2()    
    
