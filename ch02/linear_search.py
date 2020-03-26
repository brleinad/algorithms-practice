import random

def linear_search(val):
    for i in range(len(A)):
        if val == A[i]:
            return i
    return None

#A = list(range(10))
#random.shuffle(A)
#print("This is the array:")
#print(A)
#print(linear_search(3))

