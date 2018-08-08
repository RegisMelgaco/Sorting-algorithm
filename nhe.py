import matplotlib.pyplot as plt
from random import randint
import timeit

def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas"):
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

def insertion_sort (ul):
    len_ul = len(ul)
    i = 1
    while (i < len_ul):
        if ul[i] < ul[i-1]:
            j = i
            while (ul[j] < ul[j-1]):
                buffer = ul[j]
                ul[j] = ul[j-1]
                ul[j-1] = buffer
                if j > 1:
                    j -= 1
        i += 1
    return ul

size = [1000, 20000, 40000, 60000, 80000, 100000]
time = []

for s in size:
    time.append(timeit.timeit("insertion_sort({})".format(generateList(s)), setup="from __main__ import insertion_sort", number=1))
    print(s)

desenhaGrafico(size, time, "Numbers", "Time")