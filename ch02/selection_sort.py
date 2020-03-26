import random

def selection_sort(a):
    for i in range(len(a)):
        mina = a[i]
        swap = False
        for j in range(i+1, len(a)):
            if mina > a[j]:
                mina = a[j]
                k = j
                swap = True
        if swap:
            a[k] = a[i]
            a[i] = mina
    return a

#a = list(range(20))
#random.shuffle(a)
#print("array before sort:")
#print(a)
#print("array after sort:")
#print(selection_sort(a))
