# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    maxA = 0
    maxB = 0
    for num in range(n):
        if num > maxA :
            maxB = maxA
            maxA = num

    return maxB*maxA


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
