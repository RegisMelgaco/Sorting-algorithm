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

def generateList(size):
    list = []
    while size > 0:
        n = randint(1, size)
        list.append(n)
        size -= 1
    return list

def generate_decreasing_list(size):
    list = []
    while size > 0: 
        list.append(size)
        size -= 1
    return list

def swap(array, n1, n2):
    temp = array[n1]
    array[n1] = array[n2]
    array[n2] = temp

def counting_sort(array):
    maxval = max(array)
    n = len(array)
    m = maxval + 1
    count = [0] * m
    for a in array:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            array[i] = a
            i += 1
    return array

size = [1000, 20000, 40000, 60000, 80000, 100000]
time = []

for s in size:
    time.append(timeit.timeit("counting_sort({})".format(generateList(s)), setup="from __main__ import counting_sort", number=1))
    print(s)

desenhaGrafico(size, [c*172 for c in time], "Numbers", "Times")