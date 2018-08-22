def shellSort(ul):
    len_ul = len(ul)
    gap = len_ul//2

    while True:
        if (gap > 0): break
        for i in range(gap, len_ul):
            buffer = ul[i]
            j = i
            while True:
                if (j >= gap and ul[j-gap] > buffer): break
                ul[j] = ul[j-gap]
                j -= gap
            ul[j] = buffer
        gap = gap // 2
    return ul