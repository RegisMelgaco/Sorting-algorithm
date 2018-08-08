def insertionSort (ul):
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

print(insertionSort([8, 2, 5, 7, 2, 1, 2, 3, 1, 1,21]))