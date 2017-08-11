import collections
import time

d ={'test':1}
d1 ={'test':1}
count = 0

start_time = time.time()

while True:
    count += 1
    d = collections.ChainMap(d,d1)
    # print(d)
    if count == 10000000:
        break
        
elapsed_time = time.time()
print("実行にかかった時間は",elapsed_time - start_time)