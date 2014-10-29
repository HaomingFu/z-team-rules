#!/usr/bin/env python
# encoding: utf-8

def canJump(A):
    n = len(A)
    if n<= 1:
        return True

    if A[0] == 0:
        return False

    zeros=[]
    for i in range(1, n-1):
        if A[i]==0 and A[i+1]!=0:
            zeros.append(i)
    if A[-1]==A[-2] and A[-1]==0:
        zeros.append(n-2)

    if not zeros:
        return True

    last =-1
    for ix in zeros:
        if not isJump(A, last, ix):
            return False
        last = ix
    return True

def isJump(A,last, ix):
    for i in range(last +1, ix):
        if A[i] > ix- i:
            return True
    return False



A =[1,0,0,1,1,2,2,0,0,0]
print(canJump(A))
