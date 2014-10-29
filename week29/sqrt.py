#!/usr/bin/env python
# encoding: utf-8

def sqrt(x):
    if x==0 or x==1:
        return x

    low, high = 1, int(x/2)
    while low <= high:
        mid = int((low + high)/2)
        if mid*mid == x:
            return mid

        elif mid*mid < x:
            if (mid+1)*(mid+1) > x:
                return mid
            else:
                low = mid + 1
        else:
            if (mid-1)*(mid-1) < x:
                return mid -1
            else:
                high = mid -1


print(sqrt(25))
