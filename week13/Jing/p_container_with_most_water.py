"""
From: https://oj.leetcode.com/problems/container-with-most-water/
Author: Jing Zhou
Date: Jun 05, 2014
Thought: This one is easy as long as ... as long as you know how to do it. It can be done in linear time
"""



class Solution:
    # @return an integer
    def maxArea(self, height):
        low = 0
        high = len(height)-1
        maxC = (high-low)*min(height[low], height[high])
        while(low < high):
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
            maxC = max(maxC, (high-low)*min(height[low], height[high]))
        return maxC
