"""
From: https://oj.leetcode.com/problems/palindrome-partitioning-ii/
Author: Jing Zhou
Date: Sep 19, 2014
Thought: DP problem. 1 D DP. Good problem
Tags: DP, string, palindrome
"""



class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        length = len(s)
        isPan = [[False]*length for _ in range(length)]
        DP = [length - i for i in range(length+1)]
        for i in range(length-1, -1, -1):
            for j in range(i, length):
                if s[i] == s[j] and (j-i < 2 or isPan[i+1][j-1]):
                    isPan[i][j] = True
                    DP[i] = min(DP[i], DP[j+1]+1)
        return DP[0]-1
