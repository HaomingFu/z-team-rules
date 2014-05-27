"""
From: https://oj.leetcode.com/problems/pascals-triangle/
Author: Jing Zhou
Date: May 25, 2014
Thought: This is easy... just two for loops
"""



class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        result = []
        for i in range(numRows):
            aList = []
            for j in range(i+1):
                if j == 0:
                    aList.append(1)
                elif j == i:
                    aList.append(1)
                else:
                    aList.append(result[i-1][j-1] + result[i-1][j])
            result.append(aList)
        return result
