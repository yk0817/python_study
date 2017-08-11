import time

dict = {'test':1}
dict1 = {'test':1}

count = 0

start_time = time.time()

while True:
    count += 1
    dict.update(dict1)
    # print(dict)
    if count == 10000000:
        break
        
elapsed_time = time.time()
print("実行にかかった時間は",elapsed_time - start_time)