# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

# intersection finds the intersection of two segments
def intersection(seg1, seg2):
    # If any of the segmnet is None return the other segment
    if seg1 is None :
        return seg2
    if seg2 is None :
        return seg1
    # takes two segments of named tuple segment and return the intersection part as a segment named tuple
    start = max(seg1.start, seg2.start) # We took max first as we want to move foreward in number line
    end = min(seg1.end, seg2.end)
    if start <= end:
        return Segment(start, end)
    return None # Not able to form the intersection
    
def optimal_points(segments):
    #write your code here
    srtd = sorted(segments)
    # print(srtd)
    # print(type(srtd))
    ptr = 0
    intr = None
    interList = []

    while ptr < len(srtd):
        intrPrev = intr
        intr = intersection(intr, srtd[ptr])
        # print("PTR = ", ptr)
        # print("INTR = ", intr)
        # print("INTRLIST = ", interList)
        if intr is None :
            interList.append(intrPrev)
            intr = srtd[ptr]
        ptr += 1
    interList.append(intr)
    pts = []
    for x in interList:
        pts.append(x.end)
    # print("PTS = ", pts)

    return pts



        

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



