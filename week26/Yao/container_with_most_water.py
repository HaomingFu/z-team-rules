#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @return an integer
    def maxArea(self, height):
        maxVal = 0
        i , j =0, len(height)-1
        while i < j:
            val = (j-i)*min(height[i], height[j])
            mavVal = max(val, maxVal)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxVal

