import threading,time

class MyThread(threading.Thread):
    def __init__(self,count):
        threading.Thread.__init__(self)
        self.count = count
        self.return_value = None

    def run(self):
        sum_value = 0
        for i in range(1,1 + self.count):
            sum_value += i
            time.sleep(0.1)
        self.return_value = sum_value

    def get_value(self):
        return self.return_value

thread1 = MyThread(5)
thread1.start()
thread1.join()
print(thread1.return_value)  # 15 →インスタンス変数として取得
print(thread1.get_value())   # 15 →メソッドで取得
