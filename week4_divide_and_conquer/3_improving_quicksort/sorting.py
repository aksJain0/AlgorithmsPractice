# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    x = a[l]
    j = 1
    k = j
    cnt = 1
    for i in range(l+1, r+1):
        if a[i] < x :
            if k == j:
                j += 1
                k = j
                a[i], a[j] = a[j], a[i]
            else:
                k += 1
                j += 1
                a[k], a[j] = a[j], a[k]
                a[i], a[j] = a[j], a[i]

        elif a[i] == x:
            k += 1
            a[i], a[k] = a[k], a[i]          

    a[l], a[j] = a[j], a[l]
    return (j,k)

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    #m = partition2(a, l, r)
    j,k = partition3(a,l, r)
    randomized_quick_sort(a, l, j-1);
    randomized_quick_sort(a, k+1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
