from multiprocessing import Process,Pipe
import os

global test_num
# test_num = 0

def sender(conn):
    global test_num
    conn.send(test_num)
    conn.close()

def receiver(conn):
    # 他子プロセスからメッセージを受信して表示
    test_num = conn.recv()
    print('メッセージを受信:{0}'.format(test_num))
    # global test_num 
    test_num += 1
    print(test_num)
    conn.send(test_num)
    conn.close()

def main():
    parent_conn,child_conn = Pipe()
    
    while True:
        # メッセージを送信
        p_sender = Process(target=sender,args=(child_conn,))
        p_sender.start()
        # メッセージを受信
        p_receiver = Process(target=receiver,args=(parent_conn,))
        p_receiver.start()
    # p.join()
    
if __name__ == '__main__':
    main()