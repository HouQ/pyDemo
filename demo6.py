import thread
import time

def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print  threadName, time.ctime(time.time())

try:
    thread.start_new_thread(print_time,("Thread-1",1))
    thread.start_new_thread(print_time,("Thread-2",2))
except:
    print "Error"

while 1:
    pass