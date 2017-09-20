# coding:utf-8
import socket
import threading
import time


def tcplink(sock, addr):
    print 'Accept new connecyion from %s:%s...' % addr
    sock.send('welcome')
    while 1:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('hello,%s' % data)
    sock.close()
    print 'Connection from %s:%s closed' % addr


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)  # 最大连接数5
print 'Waiting for connection...'
while 1:
    # 接受一个新连接
    sock, addr = s.accept()
    # 新线程处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
