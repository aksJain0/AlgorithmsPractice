# Uses python3
import sys
import random
from functools import reduce

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm(a,b):
    factors = [] # list of factor
    i = 2
    while i <= min(a,b) :
        #print("for itertion i = ",i,"factors = ",factors)
        if (a % i == 0 or a == 1) and ( b % i == 0 or b == 1) :
            factors.append(i)
            a = a/i
            b = b/i
        else :
           i += 1

        
    factors.append(a)
    factors.append(b)
    #print("final", factors)
    return int(reduce((lambda x, y: x * y), factors))

        


if __name__ == '__main__':

    # ## Setup for stress test
    # while 1 :
    #     a = random.randrange(1,199)
    #     b = random.randrange(1,199)
    #     ln = lcm_naive(a,b)
    #     l = lcm(a,b)
    #     if(l==ln):
    #         print("OK!")
    #     else:
    #         print (a,b,"NOT OK!!", "naive=", ln, "lcm = ", l)
    #         break

    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

