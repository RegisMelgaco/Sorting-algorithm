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

def insertion_sort(array):
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
        return insertion_sort(less) + equal + insertion_sort(greater)
    else:
        return array

size = [10, 200, 400, 600, 800, 1000]
time = []

for s in size:
    time.append(timeit.timeit("insertion_sort({})".format(generate_decreasing_list(s)), setup="from __main__ import insertion_sort", number=1))
    print(s)

desenhaGrafico(size, time, "Numbers", "Time")