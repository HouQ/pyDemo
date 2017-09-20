#coding=utf-8
#支持中文编码

#列表
list = ['a',1,'2',"what's your name?"]
list1 = [1234,'john']

print list
print list[3][2:]
print list * 2
print list + list1

#元组
#类似于列表，只是不能更改，只可读取,用()标识
tuple = ('a',2,'g',3)
tuple1 = ('a',2)

print tuple
print tuple[0]
print tuple[1:3]
print tuple + tuple1

#字典
#键值对
dict = {}
dict['one'] = 'this is one'
dict[2] = 'this is two'

dict1 = {'name':'john','code':123,'dept':'party'}

print dict['one']
print dict[2]
print dict1

print dict.keys()
print dict1.values()
