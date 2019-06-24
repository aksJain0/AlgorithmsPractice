# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    currentFill = 0 
    numFills = 0
    stops.insert(0,0)
    stops.append(distance)
    n = len(stops)
    #print("stops",stops, n)
    while currentFill < n-1 :
        lastFill = currentFill
        try:
            while currentFill < n-1 and (stops[currentFill + 1] - stops[lastFill] <= tank):
                currentFill += 1
        except:
            print("out of range",currentFill,lastFill, numFills)
            
        if currentFill == lastFill:
            return -1
        elif currentFill < n-1:
            numFills += 1
    return numFills

if __name__ == '__main__':
    all =  list(map(int, sys.stdin.read().split()))
    d, m, _, stops = all[0], all[1], all [2], all [3:]
    print(compute_min_refills(d, m, stops))
