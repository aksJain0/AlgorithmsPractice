# Uses python3
import sys
import random

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fibonacci_sum(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)%10
        sum = (sum + current) %10

    return sum

if __name__ == '__main__':

    # while(1):
    #     n = random.randrange(1,100)
    #     if(fibonacci_sum(n) != fibonacci_sum_naive(n) ):
    #         print("NOT OK!")
    #         break

    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
