"""
From: http://oj.leetcode.com/problems/triangle/
Author: Jing Zhou
Date: May 18, 2014
Thought: Dynamic programming... But there's a better one...
"""



class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        l = len(triangle)
        matrix = [[0]*l for i in range(l)]
        matrix[0][0] = triangle[0][0]
        for i in range(1, l):
            matrix[i][0] = triangle[i][0] + matrix[i-1][0]
        for j in range(1, l):
            matrix[j][j] = matrix[j-1][j-1] + triangle[j][j]
        for i in range(1, l):
            for j in range(1, i):
                matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j]) + triangle[i][j]
        return min(matrix[l-1])
