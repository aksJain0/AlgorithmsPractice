# Uses python3
import sys
import random

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_lemma(a, b):
    if a < b :
        # Swap a and b
        a = a + b
        b = a - b
        a = a - b
    # Now we are sure that a > b

    an = a % b

    if an == 0 :
        return b

    else :
        return gcd_lemma(b, an)

if __name__ == "__main__":

    # ## Stress Test
    # while(1):
    #     a, b = random.randrange(1,1000), random.randrange(1,1000)

    #     if gcd_naive(a,b) != gcd_lemma(a,b):
    #         print('a = ', a, 'b = ', b, 'naive = ', gcd_naive(a,b), 'lemma = ', gcd_lemma(a,b))
    #         break
    #     else :
    #         print("OK!")

    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_lemma(a, b))
