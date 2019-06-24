# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = set()
    #write your code here
    srtd = sorted(segments)
    # print(srtd)
    # print(type(srtd))
    current = 0
    previous = 0
    point = 1000000000  # 10^9
    while current < len(srtd):
        # print("c =", current)
        # print(points)
        if srtd[current].start == srtd[previous].start:
            point = min(point,srtd[current].end)
            previous = current 
            current = current + 1
        elif srtd[current].start > point:
            points.add(point)
            point = srtd[current].end
            previous = current
            current = current + 1
        else:
            #print("appending point")
            points.add(point)
            previous = current
            current = current + 1
            

    return list(points)

if __name__ == '__main__':
    input = sys.stdin.read()
    #print(input)
    n, *data = (map(int, input.split()))
    # n = all[0]
    # data = all[1:]
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')



