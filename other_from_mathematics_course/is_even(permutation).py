def is_even(p):
    # function to check if the given permutation is even 
    # i.e.: Can it be sorted in even number of transpositions

    status = 0 # counted as no of transpostions % 2 , Hence it will be 1 for odd number of transpositions

    si = 0 # si is positions before which p is sorted si excluded

    n = len(p)

    while (si < n) :
        smallest = si # contains the index of smallest element in p[si:]
        print(p)
        for i in range(si,n) :
            
            if  p[i] < p[smallest] :
                smallest = i

        if smallest != si :        
            p[si] = p[si] + p[smallest]
            p[smallest] = p[si] - p[smallest]
            p[si] = p[si] - p[smallest]
            status = (status + 1) % 2
        si += 1      
        
    
    return False if status else True


if __name__ == '__main__':
    p = list(map(int, input().split()))
    #p =  [0,3,2,4,5,6,7,1,9,8]
    print(is_even(p))    
