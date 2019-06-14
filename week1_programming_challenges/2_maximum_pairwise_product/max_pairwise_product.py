# python3


def max_pairwise_product(numbers):
    maxA = 0
    maxB = 0
    for num in numbers:
        if num > maxA :
            maxB = maxA
            maxA = num
        elif num > maxB :
            maxB = num

    return maxB*maxA


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
