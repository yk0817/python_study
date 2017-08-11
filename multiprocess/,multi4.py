from multiprocessing import Process

def f(i):
    print('{0}番目のプロセス実行中'.format(i))

def main():
    for i in range(100):
        p = Process(target=f,args=(i,))
        p.start()
    p.join()

if __name__ == '__main__':
    main()