# Uses python3
import sys
import random

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def fib_start_last_digit(n):
    #To get previous and current values other that start of the fibonacci series

    previous = 0
    current = 1

    for i in range(n-1):
        previous, current = current, (current + previous)%10

    return previous, current


def fibonacci_partial_sum(from_, to):
    sum = 0

    previous, current = fib_start_last_digit(from_)
    #print("current = ", current)
    for i in range(to-from_+1):
        sum = (sum + current)%10
        previous, current = current, (current + previous)%10
        

    return sum


if __name__ == '__main__':
    # random.seed(1009)
    # while 1 :
    #     frm = random.randint(1,10)
    #     to = random.randint(10,100)
    #     fn = fibonacci_partial_sum_naive(frm,to)
    #     f = fibonacci_partial_sum(frm,to)
    #     if(f == fn):
    #         print("OK!")
    #     else:
    #         print(frm,to , "NOT OK!!", "fn = ", fn, "f = ", f)
    #         break;


    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))