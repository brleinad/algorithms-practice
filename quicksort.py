def quicksort(array_in):
    """My quick implementation of quick sort in Python.
    Input a list.
    Output a sorted list."""
    array = list(array_in)
    if len(array) == 1:
        return array
    if len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array
    
    pivot = len(array)-1
    i = 0
    while i < pivot:
        if array[i] > array[pivot]:
            array[i], array[pivot-1], array[pivot] = array[pivot-1], array[pivot], array[i]
            pivot -= 1
        else:
            i += 1

    if pivot == 0:
        array[1:] = quicksort(array[1:])
    elif pivot == len(array)-1:
        array[:pivot] = quicksort(array[:pivot])
    else:
        array[:pivot] = quicksort(array[:pivot])
        array[pivot+1:] = quicksort(array[pivot+1:])
        
    
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

print quicksort(test)
