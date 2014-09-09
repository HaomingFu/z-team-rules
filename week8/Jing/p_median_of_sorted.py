"""
From: http://oj.leetcode.com/problems/median-of-two-sorted-arrays/
Author: Jing Zhou
Date: April 30, 2014
Thought: This is quite easy. Just construct another array. and get the middle element or average of the middle 2 elements.
"""
class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        i, j = 0, 0
        C = []
        while(i < len(A) and j < len(B)):
            if A[i] <= B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        C.extend(A[i:]) if j==len(B) else C.extend(B[j:])
        if len(C)%2 == 1:
            return C[len(C)/2]
        else:
            return (C[len(C)/2]+C[len(C)/2-1])/float(2)
