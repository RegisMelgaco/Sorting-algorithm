import functools
import random

def regis_sort(ul):

    print("ul", ul)
    
    average = functools.reduce(lambda a, n: a+n, ul, 0) / len(ul)

    bigger, smaller = [], []

    for n in ul:
        bigger.append(n) if n >= average else smaller.append(n)

    len_bigger, len_smaller = len(bigger), len(smaller)

    bigger = regis_sort(bigger) if len_bigger > 1 and not len_bigger == bigger.count(bigger[0]) else bigger
    smaller = regis_sort(smaller) if len_smaller > 1 and not len_smaller == smaller.count(smaller[0]) else smaller

    return smaller + bigger

generate_ul = lambda size = 30, biggest_number = 20, smallest_number = -20 : [random.randint(smallest_number, biggest_number) for i in range(size)]

for i in range(100):
    regis_sort(generate_ul())