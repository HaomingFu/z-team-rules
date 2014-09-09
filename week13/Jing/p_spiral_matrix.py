"""
From: https://oj.leetcode.com/problems/spiral-matrix-ii/
Author: Jing Zhou
Date: Jun 04, 2014
Thought: The same with the first problem with minimum changes
"""



class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n == 0:
            return []
        matrix = [[0]*n for _ in range(n)]
        self.spiralMatrix(matrix, n, n, 0, 1)
        return matrix
    def spiralMatrix(self, matrix, m, n, k, start):
        if (m<=0 or n<=0):
            return
        if m == 1:
            for j in range(n):
                matrix[k][k+j] = start
                start += 1
            return
        if n == 1:
            for i in range(m):
                matrix[k+i][k] = start
                start += 1
            return
        for i in range(n-1):
            matrix[k][k+i] = start
            start += 1
        for i in range(m-1):
            matrix[k+i][k+n-1] = start
            start += 1
        for i in range(n-1):
            matrix[k+m-1][k+n-1-i] = start
            start += 1
        for i in range(m-1):
            matrix[k+m-1-i][k] = start
            start += 1
        self.spiralMatrix(matrix, m-2, n-2, k+1, start)
