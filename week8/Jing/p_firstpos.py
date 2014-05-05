"""
From: http://oj.leetcode.com/problems/first-missing-positive/
Author: Jing Zhou
Date: May 3, 2014
Thought: This one nearly killed me... I spent quite a while trying
To get the index right. May rewrite it soon.
"""
class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if not A:
            return 1
        length = len(A)
        i, j = 0, length-1
        while(i<j):
            if A[i] <= 0 and A[j] > 0:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
            elif A[i] > 0 and A[j]<= 0:
                j -= 1
                i += 1
            elif A[i] > 0 and A[j] > 0:
                i += 1
            elif A[i] <= 0 and A[j] <= 0:
                j -= 1
        new_len = sum([1 for item in A if item > 0])
        for k in range(new_len):
            if abs(A[k]) <= length and A[abs(A[k])-1] > 0 :
                A[abs(A[k])-1] = -A[abs(A[k])-1]
        for m in range(max(1, new_len)):
            if A[m] >= 0:
                return m + 1
        return length+1 if m==length-1 else m+2
