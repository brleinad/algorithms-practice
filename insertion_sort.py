import random

def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i+1] = key
    return a

#a = list(range(30))
#random.shuffle(a)
#print("array before sort:")
#print(a)
#print("array after sort:")
#print(insertion_sort(a))
    
