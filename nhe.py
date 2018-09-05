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

def radix_sort(ul):
    len_ul = len(ul)
    modulus = 10
    div = 1
    while True:
        new_list = [[], [], [], [], [], [], [], [], [], []]
        for value in ul:
            least_digit = value % modulus
            least_digit = least_digit // div
            new_list[least_digit].append(value)
        modulus = modulus * 10
        div = div * 10
        if len(new_list[0]) == len_ul:
            return new_list[0]
        ul = []
        rd_list_append = ul.append
        for x in new_list:
            for y in x:
                rd_list_append(y)

size = [1000, 20000, 40000, 60000, 80000, 100000]
time = []

for s in size:
    time.append(timeit.timeit("radix_sort({})".format(generateList(s)), setup="from __main__ import radix_sort", number=1))
    print(s)

desenhaGrafico(size, [c*172 for c in time], "Numbers", "Times")