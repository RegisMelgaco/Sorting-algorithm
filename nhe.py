import matplotlib.pyplot as plt
from random import randint
import timeit

import sys
sys.setrecursionlimit(1000000)

def desenhaGrafico(x,y,xl = "Entradas", yl = "Saida"):
    plt.plot(x,y, label = "Melhor Tempo")
    plt.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()  

generate_ul = lambda size = 30, biggest_number = 20, smallest_number = -20 : [randint(smallest_number, biggest_number) for i in range(size)]

def generate_decreasing_list(size):
    list = []
    while size > 0: 
        list.append(size)
        size -= 1
    return list

def generateList(s):
    return [randint(0,10000) for c in range(s)]

import functools

def bucket_sort(ul):
    largest = max(ul)
    length = len(ul)
    size = largest/length
 
    buckets = [*map(lambda x : [], ul)]
    for i in range(length):
        j = int(ul[i]/size)
        
        buckets[j].append(ul[i]) if j != length else buckets[length - 1].append(ul[i])            
 
    for i in range(length):
        quick_sort(buckets[i])
 
    result = []
    for i in range(length):
        result = result + buckets[i]
 
    return result

def quick_sort(array=[12,4,5,6,7,3,1,15]):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return array


size = [1000, 20000, 40000, 60000, 80000, 100000]
time = []

for s in size:
    time.append(timeit.timeit("bucket_sort({})".format(generateList(s)), setup="from __main__ import bucket_sort", number=1))
    print(s)

desenhaGrafico(size, [c*172 for c in time], "Numbers", "Times")