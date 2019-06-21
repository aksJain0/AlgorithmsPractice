# Uses python3
import sys
import math

def get_change(m):
    #write your code here
    r = m
    n = 0

    for e in [10, 5, 1]:
        if r == 0:
            return n
        nc = math.floor(r/e)
        n = n + nc
        r = r - ( e * nc )
    return int(n)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
