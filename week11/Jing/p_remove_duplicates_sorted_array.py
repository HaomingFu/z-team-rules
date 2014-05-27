"""
From: https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
Author: Jing Zhou
Date: May 21, 2014
Thought: I created another array but I doubt that's necessary at all
"""



class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) <= 2:
            return len(A)
        B = [A[0], A[1]]
        for i, val in enumerate(A):
            if i >= 2 and val != -99999:
                if val == A[i-1] and val == A[i-2]:
                    flag = A[i]
                    A[i] = -99999
                elif A[i-1] == -99999 and A[i] == flag:
                    A[i] = -99999
                else:
                    B.append(A[i])
        A[:len(B)] = B
        return len(B)
