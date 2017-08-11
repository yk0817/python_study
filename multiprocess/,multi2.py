from multiprocessing import Process,Queue

def sender(q,n):
    q.put('{0}回目のhello world!'.format(n))

def main():
    q = Queue()
    for i in range(5):
        p = Process(target=sender,args=(q,i))
        p.start()
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    
    p.join()

if __name__ == '__main__':
    main()