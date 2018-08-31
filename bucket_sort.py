import functools

def bucket_sort(ul):
    largest = max(ul)
    length = len(ul)
    size = largest/length
 
    buckets = [*map(lambda x : [], ul)]
    for i in range(length):
        j = int(ul[i]/size)
        
        buckets[j].append(ul[i]) if j != length else buckets[length - 1].append(ul[i])            
 
    for i in range(length):
        quick_sort(buckets[i])
 
    result = []
    for i in range(length):
        result = result + buckets[i]
 
    return result

def quick_sort(array=[12,4,5,6,7,3,1,15]):
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
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return array

print(bucket_sort([7, 2, 9, 1, 0, 4, 7, 6, 2, 8, 9, 1, 2, 4 , 1]))