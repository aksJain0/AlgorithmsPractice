# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    mid = left + ((right-left) // 2)
    ml = get_majority_element(a, left, mid)
    mr = get_majority_element(a, mid+1, right)

    if ml != -1:
        count = 0
        for e in a[left:right]:
            # print("checking for ml = ", ml," in a[",left,right,"] against", e)
            if e == ml:
                count += 1
        # print("count of ml = ", ml, "count = ", count, "checking against = ", (right-left)//2)
        if count > (right - left)//2:
            # print("Returning ml = ",ml)
            return ml

    if mr != -1:
        count = 0
        for e in a[left:right]:
            # print("checking for mr = ", mr, " in a[",left,right,"] against" ,e)
            if e == mr:
                count += 1
        # print("count of mr = ", mr, " count = ", count, "checking against = ", (right-left))
        if count > (right - left)//2:
            # print("returning mr = ", mr)
            return mr    
        


    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
