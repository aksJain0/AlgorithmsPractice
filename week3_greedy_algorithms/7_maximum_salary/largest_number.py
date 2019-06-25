#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    srtd = sorted(a,  key = len)
    srtd = sorted (srtd, key = lambda x : x[0], reverse = True)
        
    for x in srtd:
        res += x
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
