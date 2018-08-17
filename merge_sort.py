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

print(mergeSort([2, 4, 3, 1, 5, 4, 1, 2, 1, 1]))