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

def mergeSort(ul):
    if len(ul) > 1:
        mid = len(ul) // 2

        left_ul = ul[:mid]
        right_ul = ul[mid:]

        mergeSort(left_ul)
        mergeSort(right_ul)

        i = 0
        j = 0
        k = 0

        while i < len(left_ul) and j < len(right_ul):

            if left_ul[i] < right_ul[j]:
                ul[k]=left_ul[i]
                i += 1
            else:
                ul[k]=right_ul[j]
                j += 1
            k += 1

        while i < len(left_ul):

            ul[k]=left_ul[i]
            i += 1
            k += 1

        while j < len(right_ul):
            ul[k]=right_ul[j]
            j += 1
            k += 1
    return ul

size = [1000, 20000, 40000, 60000, 80000, 100000]
time = []

for s in size:
    time.append(timeit.timeit("mergeSort({})".format(generateList(s)), setup="from __main__ import mergeSort", number=1))
    print(s)

desenhaGrafico(size, time, "Numbers", "Time")