 # collectionsモジュール勉強
import collections
c = collections.Counter()
c['spam'] += 1
c[100] += 1
c[200] += 2
c[200] += 3
# Counter({200: 5, 'spam': 1, 100: 1})
print(type(c))
c2 = collections.Counter()
c2['spam'] = 1
c2[200] = 1

print(c & c2) #Counter({200: 1, 'spam': 1})
print(c + c2) #Counter({200: 6, 'spam': 2, 100: 1})

d1 ={'spam':1}
d2 ={'ham':2}
d = collections.ChainMap(d1,d2)
print(d)