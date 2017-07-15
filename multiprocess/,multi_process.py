import multiprocessing
import os

def do_this(what):
    whoami(what)

def whoami(what):
    print("process %s says: %s" % (os.getpid(),what))

if __name__ == "__main__":
    whoami("i am the main program")
    for n in range(4):
        p = multiprocessing.Process(target=do_this,args=("i am function %s" % n,))
        p.start()