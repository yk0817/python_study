import pickle
from singer import Singer

singer = Singer('Shanranran')

with  open('singer.pickle','wb') as f:
    pickle.dump(singer,f)