#!/usr/bin/env python
# encoding: utf-8

def maxSubArray(A):
    max_so_far ,max_end_here =A[0], 0
    for each in A:
        max_end_here = max(each, max_end_here + each)
        max_so_far = max(max_so_far, max_end_here )
    return max_so_far

if __name__ ==  "__main__":
    A = [-1, 0]
    print(maxSubArray(A))


