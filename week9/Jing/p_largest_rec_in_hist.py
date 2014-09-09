"""
From: http://oj.leetcode.com/problems/largest-rectangle-in-histogram/
Author: Jing Zhou
Date: May 12, 2014
Thought: This algorithm is still O(n*n) but because a little change it passed the judge.
"""


class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        if not height:
            return 0
        maxArea = 0
        for i in range(len(height)):
            minV = height[i]
            if i+1 < len(height) and height[i] <= height[i+1]:
                continue
            for j in range(i, -1, -1):
                minV = min(minV, height[j])
                area = minV*(i-j+1)
                if area > maxArea:
                    maxArea = area
        return maxArea
