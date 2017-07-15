# python3入門 P333
import multiprocessing as mp

def washer(dishes,output):
    for dish in dishes:
        print('Washing', dish,'dish')
        output.put(dish)

def dryer(input):
    while True:
        dish = input.get()
        print('Drying',dish,'dish')
        input.task_done()

dish_queue = mp.JoinableQueue()
dryer_proc = mp.Process(target=dryer,args=(dish_queue,))
dryer_proc.daemon = True
dryer_proc.start()

dishes = ['salad','bread','entree','dessert']
dish_queue.join()