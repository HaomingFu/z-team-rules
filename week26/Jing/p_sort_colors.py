"""
Author: Jing Zhou

"""
def sort_it(array):
    """takes a list of values of 1, 2, 3
    and return a sorted list
    requirements: go through the list only once
    use constant space
    Idea: taken from http://www.ocf.berkeley.edu/~wwu/cgi-bin/yabb/YaBB.cgi?board=riddles_cs;action=display;num=1100111371
    Lo := 1; Mid := 1; Hi := N;
    while Mid <= Hi do
        Invariant: a[1..Lo-1]=0 and a[Lo..Mid-1]=1 and a[Hi+1..N]=2; a[Mid..Hi] are unknown.
        case a[Mid] in
        0: swap a[Lo] and a[Mid]; Lo++; Mid++
        1: Mid++
        2: swap a[Mid] and a[Hi]; Hi--
    """
    low = mid = 0
    high = len(array)-1
    while high > mid:
        while array[high] == 3:
            high -= 1
        if array[mid] == 1:
            array[low], array[mid] = array[mid], array[low]
            low += 1
            mid += 1
        elif array[mid] == 2:
            mid += 1
        elif array[mid] == 3:
            array[mid], array[high] = array[high], array[mid]
            high -= 1
    return array

print(sort_it([1,2,3,2,1,3,3,2,2,2,1]))


