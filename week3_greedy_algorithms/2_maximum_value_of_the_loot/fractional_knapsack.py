# Uses python3
import sys



def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here

    lst_tups = zip(values, weights)

    lst_tups_sorted = sorted(lst_tups, key = lambda x : x[0] / x[1], reverse = True)

    for e in lst_tups_sorted:
        if capacity == 0:
            return value
        a = min(e[1], capacity)
        value += a * ( e[0] / e[1] )
        capacity -= a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
