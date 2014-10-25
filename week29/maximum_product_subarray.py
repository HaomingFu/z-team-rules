#!/usr/bin/env python
# encoding: utf-8

def maxProduct(A):
    n = len(A)
    if n ==1:
        return A[0]
    maxLast= minLast= A[0]
    maxRes = A[0]
    for each in A[1:]:
        maxCur= max(each*maxLast, minLast*each, each)
        minCur= min(each*maxLast, each*minLast, each)
        maxRes = max(maxRes, maxCur)
        maxLast = maxCur
        minLast = minCur
    return maxRes


A = [-4, -3, -2]
print(maxProduct(A))


