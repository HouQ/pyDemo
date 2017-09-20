#coding=utf-8
list = []
for x in range(100):
    for i in range(2,x):
        if x % i == 0:
            # j = x/i
            # print "%d = %d * %d" %(x,i,j)
            break
    else:
       	list.append(x)
print list


from copy import deepcopy

dict = {'name':'hou','age':29,'hobby':[1,2,3]}
dict1 = dict.copy()
dict2 = deepcopy(dict)
dict['hobby'] = [1,2,3,4]
print dict['hobby']
print dict1['hobby']
print dict2['hobby']