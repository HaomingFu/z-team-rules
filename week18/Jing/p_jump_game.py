"""
From: https://oj.leetcode.com/problems/jump-game/
Author: Jing Zhou
Date: Jul 18, 2014
Thought: Passed at first try... But it's a simple problem after all
Tags: array, list, numbers
"""



class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if len(A) <= 1:
            return True
        can = [False]*(len(A)-1)
        can.append(True)
        lastTrue = len(A)-1
        for i in range(len(A)-2, -1, -1):
            if A[i]+i >= lastTrue:
                can[i] = True
                lastTrue = i
        return can[0]
