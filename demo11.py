import time
def get_local_time():
    localtime = time.localtime(time.time())
    return localtime[0:6]
print get_local_time()
