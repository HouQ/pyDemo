# coding:utf-8

# class Champion():
#     '''a champion in lol'''
#     count = 0
#     def __init__(self,name,**kw):
#         self.name = name
#         for k,v in kw.iteritems():
#             self.k = v
#         Champion.count += 1
#     def claim(self):
#         print self.name,self.__class__,self.__doc__

# garen = {'sex':'male','land':'zone1','speed':350}
# ashe = {'sex':'female','land':'zone2','speed':370}

# g = Champion('Garen',**garen)
# a = Champion('Ashe',**ashe)
# g.claim()
# a.claim()
# print Champion.count


# class Student():
#     count = 0
#     def __init__(self):
#         Student.count += 1
#         print Student.count,'student instance created'

# class Teacher(object):
#     count = 0
#     def __init__(self):
#         Teacher.count += 1
#         print Teacher.count,'teacher instance created'

# print dir(Student)
# print dir(Teacher)

# s = Student()
# t = Teacher()

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer =[]
while 1:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)

s.close()

header,html = data.split('\r\n\r\n',1)
print header
with open('sina.html','wb') as f:
    f.write(html)
