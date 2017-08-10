import threading
import time

class TimeThread(threading.Thread):
    def __init__(self, arg):
        threading.Thread.__init__(self)


    def run(self):
        global


def main():
    start_time = time.time()
    # 処理作業を書く
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)

if __name__ == '__main__':
    main()
