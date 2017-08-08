import threading,time

class MyThread(threading.Thread):
    def __init__(self, name,sleep_time):
        threading.Thread.__init__(self)
        self.name = name
        self.sleep_time = sleep_time

    def run(self):
        for i in range(10):
            print(self.name + ':' + str(i))
            time.sleep(self.sleep_time)

thread1 = MyThread('A',1)
thread2 = MyThread('B',1)

thread1.start()
thread2.start()
