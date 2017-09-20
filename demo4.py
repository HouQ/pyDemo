#coding=utf-8

from copy import deepcopy
d1 ={'name':'Bob','age':25,'hobby':[1,2,3]}	#元字典
d2 = d1.copy()	#浅拷贝
d3 = deepcopy(d1)	#深拷贝

d1['hobby'].append(4)
d1['hobby'].remove(1)
print '元字典',d1,'\n','浅拷贝',d2,'\n','深拷贝',d3

# .copy() 浅拷贝只是引用，对元字典操作会影响浅拷贝对象
# deepcopy() 深拷贝与元字典互不影响

#参数传递
a = 1
b = [1,2,3]

def change(x,y):
	x = x + 1
	y.append(x)
	print x
	print y

change(a,b)
print a
print b


def reverse(li):
	for i in range(len(li)/2):
		li[i],li[-(i+1)] = li[-(i+1)],li[i]

	print li
li = [1,2,3,4,5,6]
reverse(li)