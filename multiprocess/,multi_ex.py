# http://iatlex.com/python/parallel_first/
from multiprocessing import Pool

def nijou(x):
    print( x*x )

if __name__ == '__main__':
    p = Pool(4)
    p.map(nijou,range(10000))
