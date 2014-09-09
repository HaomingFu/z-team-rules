"""
From: https://oj.leetcode.com/problems/set-matrix-zeroes/
Author: Jing Zhou
Date: Jun 10, 2014
Thought: Traverse twice. There might be a way to do it once but this one is clear enough and has a good running time already
"""



class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if not matrix:
            return matrix
        zeros = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros.add((i, j))
        for i, j in zeros:
            for m in range(len(matrix[0])):
                matrix[i][m] = 0
            for n in range(len(matrix)):
                matrix[n][j] = 0
