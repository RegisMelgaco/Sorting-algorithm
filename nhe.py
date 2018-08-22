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

def shellSort(ul):
    len_ul = len(ul)
    gap = len_ul//2
    count = 0

    while True:
        if (gap > 0): break
        for i in range(gap, len_ul):
            buffer = ul[i]
            j = i
            while True:
                if (j >= gap and ul[j-gap] > buffer): break
                ul[j] = ul[j-gap]
                j -= gap
                count += 1
            ul[j] = buffer
        gap = gap // 2
    return count

size = [1000, 20000, 40000, 60000, 80000, 100000]
time = []
counts = []

for s in size:
    time.append(timeit.timeit("shellSort({})".format(generateList(s)), setup="from __main__ import shellSort", number=1))
    print(s)

for s in size:
    counts.append(shellSort(generateList(s)))

print(counts)

desenhaGrafico(size, counts, "Numbers", "Count")