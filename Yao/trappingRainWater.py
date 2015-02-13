#!/usr/bin/env python
# encoding: utf-8

class Solution:
    #@param A, a list of integer
    #@ return an integer
    def trap(self, A):
        if len(A) < 2:
            return 0
        maxL = [0]*len(A)
        maxR = [0]*len(A)
        maxCur = A[0]
        for i in range(1, len(A)):
            maxL[i] = maxCur
            maxCur = max(maxCur, A[i])
        maxR[-1] = 0
        maxCur = A[-1]
        res = 0
        for i in range(len(A) - 2, -1, -1):
            maxR[i] = maxCur
            ctrap = min(maxL[i], maxR[i]) - A[i]
            maxCur = max(maxCur, A[i])
            if ctrap > 0:
                res += ctrap
        return res




s  = Solution()
A = []
print(s.trap(A))

