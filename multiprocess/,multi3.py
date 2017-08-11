from multiprocessing import Process,Pipe
import os

def sender(conn):
    conn.send("hello world")
    conn.close()

def receiver(conn):
    # 他子プロセスからメッセージを受信して表示
    msg = conn.recv()
    print('メッセージを受信:{0}'.format(msg))
    conn.close()

def main():
    parent_conn,child_conn = Pipe()
    
    # メッセージを送信
    p = Process(target=sender,args=(child_conn,))
    p.start()
    # メッセージを受信
    p = Process(target=receiver,args=(parent_conn,))
    p.start()
    p.join()
    
if __name__ == '__main__':
    main()