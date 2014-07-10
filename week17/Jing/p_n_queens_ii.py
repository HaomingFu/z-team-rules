"""
From: https://oj.leetcode.com/problems/n-queens-ii/
Author: Jing Zhou
Date: Jul 10, 2014
Thought: It's actually easier than the first one... When you already worked the first one out.
"""



class Solution:
    # @return an integer
    def totalNQueens(self, n):
        res =[0]
        A = [-1]*n
        self.solveN(A, res, n, 0)
        return res[0]
    def solveN(self, A, res, n, cur):
        if cur == n:
            res[0] += 1
        else:
            for i in range(n):
                A[cur] = i
                if self.isValid(A, cur):
                    self.solveN(A, res, n, cur+1)
    def isValid(self, A, cur):
        for i in range(0, cur):
            if A[i] == A[cur] or abs(A[i]-A[cur]) == cur-i:
                return False
        return True
