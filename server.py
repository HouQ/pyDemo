# coding:utf-8
import socket
import threading
import time
import json


class Drink(object):
    '''Drink class'''

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


def tcplink(sock, addr):
    '''serverside'''
    cola = Drink('cola', 5, 40)
    soda = Drink('soda', 6, 30)
    lemon = Drink('lemon', 4, 20)
    mine = Drink('mine', 2, 80)
    milk = Drink('milk', 10, 30)
    listD = [cola, soda, lemon, mine, milk]
    msg = ''
    for li in listD:
        msg += li.name + ':' + str(li.price) + '|'

    print 'Accept new connecyion from %s:%s...' % addr
    sock.send(msg)
    while 1:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('hello,%s' % data)
    sock.close()
    print 'Connection from %s:%s closed' % addr


if __name__ == '__main__':
    print 'aa'
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
