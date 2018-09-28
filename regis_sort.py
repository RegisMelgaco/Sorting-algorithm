import functools
import random

def regis_sort(ul):
    
    average = functools.reduce(lambda a, n: a+n, ul, 0) / len(ul)

    bigger, smaller = [], []

    for n in ul:
        bigger.append(n) if n >= average else smaller.append(n)

    recursion = lambda li, len_li: regis_sort(li) if len_li > 1 and not len_li == li.count(li[0]) else li

    bigger = recursion(bigger, len(bigger))
    smaller = recursion(smaller, len(smaller))

    return smaller + bigger