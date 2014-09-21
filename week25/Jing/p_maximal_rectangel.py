"""
From: https://oj.leetcode.com/problems/maximal-rectangle/
Author: Jing Zhou
Date: Sep 21, 2014
Thought: Used the rectangle histogram subroutine
Tags: It's easy... as long as you think of a way to use the rectangle histogram problem
"""



class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        row, col = len(matrix), len(matrix[0])
        helpMatrix = [[0]*col for _ in range(row)]
        maxArea = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "1":
                    if i == 0:
                        helpMatrix[i][j] = 1
                    else:
                        helpMatrix[i][j] = helpMatrix[i-1][j]+1
        for i in range(row):
            max_in_row = self.largestRectangleArea(helpMatrix[i])
            if max_in_row > maxArea:
                maxArea = max_in_row
        return maxArea

    def largestRectangleArea(self, height):
        if not height:
            return 0
        i = 0
        stack = []
        maxArea = 0
        while i < len(height):
            if not stack or height[stack[-1]] <= height[i]:
                stack.append(i)
                i += 1
            else:
                h = stack[-1]
                stack.pop()
                area = height[h]*(i-stack[-1]-1 if stack else i)
                if maxArea < area:
                    maxArea = area
        while stack:
            h = stack[-1]
            stack.pop()
            area = height[h]*(i-stack[-1]-1 if stack else i)
            if maxArea < area:
                maxArea = area
        return maxArea
