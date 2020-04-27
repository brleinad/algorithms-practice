from math import floor

def merge(a, p, q, r):
    left = a[p:q]
    right = a[q+1:r]
    left.append(0)
    right.append(0)
    i, j = (0, 0,)
    print(left,right)
    for k in range(p, r-1):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
    return a

def merge_sort_rec(a, p, r):
    print(a)
    print((p,r))
    if p < r:
        q = floor((p + r)/2)
        a = merge_sort_rec(a, p, q)
        a = merge_sort_rec(a, q+1, r)
        a = merge(a, p, q, r)
    return a

def merge_sort(a):
    merge_sort_rec(a, 0, len(a)-1)

a = [4, 3, 5, 3, 1, 2]
print(a)
print(merge_sort_rec(a, 0, len(a)-1))
