"""
From: https://oj.leetcode.com/problems/n-queens/
Author: Jing Zhou
Date: Jul 10, 2014
Thought: The famous n-queens problem
"""



class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        res =[]
        A = [-1]*n
        self.solveN(A, res, n, 0)
        return res
    def solveN(self, A, res, n, cur):
        if cur == n:
            self.addToRes(A, res, n)
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
    def addToRes(self, A, res, n):
        tmp = [['.']*n for _ in range(n)]
        for i, val in enumerate(A):
            tmp[i][val] = 'Q'
        res.append([''.join(item) for item in tmp])
