import threading, time

global_counter = 5
global_lock = threading.Lock()   # LOCK OBJECT

class MyThread(threading.Thread):
    def __init__(self, name, sleep_time):
        threading.Thread.__init__(self)
        self.name = name
        self.sleep_time = sleep_time

    def run(self):
        global global_counter
        global global_lock

        # LOCK
        global_lock.acquire()

        count = global_counter
        print(self.name + ': read global_value ' + str(global_counter))
        print(self.name + ': do something')
        time.sleep(self.sleep_time)
        global_counter = count - 1
        print(self.name + ': write global_value ' + str(global_counter))

        # RELEASE
        global_lock.release()

thread1 = MyThread('A', 5)
thread2 = MyThread('B', 3)
thread1.start()
time.sleep(1)
thread2.start()

thread1.join()
thread2.join()
print('Result: ' + str(global_counter))
