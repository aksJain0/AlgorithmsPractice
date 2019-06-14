# Uses python3
def calc_fib(n):
    
    if n < 2 :
        return n
    
    a = 0
    b = 1

    for i in range(2,n+1):
        c = a + b
        a = b
        b = c
    return c

n = int(input())
print(calc_fib(n))
