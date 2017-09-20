#coding=utf-8
# list = [1,2,3]
# tu =(2,3,list)
# print tu
# list.pop()
# print tu
#元组不可变，怎么变了呢？
#变的不是元组，是元组里的列表
#本身元组里的存的是列表的引用
#引用本身没变

# def myabs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('wrong number')
#     if x >= 0:
#         print x
#     else:
#         print 0-x
# myabs('a')

# def add(x,y):
#     return x,y
# a = add(3,5)
# print a

# a = range(1,11)
# b = [x*x for x in range(1,11)]
# c = [x**3 for x in range(1,11) if x % 2 == 0]
# d = [m + n for m in 'ABC' for n in 'XYZ']
# e = {'a':1,'b':2,'c':3,'d':4}
# for k,v in e.iteritems():
#     print k,'=',v

# def swap(a):
#     if not isinstance(a,str):
#         raise TypeError("must be a string")
#     elif len(a) < 2:
#         raise TypeError("must over 2")
#     return a[0]+a[1]
# li = ['hello','what','message','learn']
# f = [swap(p) for p in li]
# g = (swap(p) for p in li)
# for i in g:
#     print ia = range(1,11)
# b = [x*x for x in range(1,11)]
# c = [x**3 for x in range(1,11) if x % 2 == 0]
# d = [m + n for m in 'ABC' for n in 'XYZ']
# e = {'a':1,'b':2,'c':3,'d':4}
# for k,v in e.iteritems():
#     print k,'=',v

# def swap(a):
#     if not isinstance(a,str):
#         raise TypeError("must be a string")
#     elif len(a) < 2:
#         raise TypeError("must over 2")
#     return a[0]+a[1]
# li = ['hello','what','message','learn']
# f = [swap(p) for p in li]
# g = (swap(p) for p in li)
# for i in g:
#     print i



# def func(a,b,c=0,*args,**kw):
#     print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw

# list = [9,8,7,6]
# dict = {'q':'a','w':'b'}

# func(1,2)
# func(1,2,c=3)
# func(1,2,3,'a','b')
# func(1,2,3,'a','b',x=1,y=30)
# func(list,dict)
# func(1,list,dict)
# func(1,2,list,dict)
# func(1,2,3,list,dict)
# func(*list)
# func(1,*list)
# func(ax=3,*list,**dict)

#map
li = ['aDam','bob','cesar','Dorethy']
def format(s):
    return s.capitalize()
print map(format,li)

#reduce实现累乘
def prod(l):
    def x(a,b):
        return a * b
    return reduce(x,l)
print prod([3,2,1])

#filter实现过滤质数
def noPn(a):
    for i in range(2,a):
        if a%i == 0:
            break
    else:
        return a
print filter(noPn,range(2,100))

#sorted实现自定义排序
def cmp_ignore_case(s1,s2):
    s1 = s1.upper()
    s2 = s2.upper()
    if s1 > s2:
        return 1
    elif s1 < s2:
        return -1
    return 0
print sorted(['Adam','bob','cathey','Dorethy'],cmp_ignore_case)