from multiprocessing import Process
import os


def f(x):
    print("{0} - プロセスID: {1} (親プロセスID: {2})".format(x,os.getpid(),os.getppid()))

def main():
    for i in range(10):
        p = Process(target=f,args=(i,))
        p.start()
        # print(p.is_alive())
    p.join()
    print(p.is_alive())

    
if __name__ == '__main__':
    main()
