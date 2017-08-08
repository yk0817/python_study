import threading,time

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(10):
            print('MyThread:' + str(i))
            time.sleep(1)

mt = MyThread()
mt.start()
for i in range(10):
    print('main:' + str(i))
    time.sleep(1)
