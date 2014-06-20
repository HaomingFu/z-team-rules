"""
From: https://oj.leetcode.com/problems/distinct-subsequences/
Author: Jing Zhou
Date: Jun 19, 2014
Thought: Basic dynamic programming...
Tags: DP, string
"""



class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        DT = [[0]*(len(T)+1) for _ in range(len(S)+1)]
        for i in range(len(S)+1):
            DT[i][0] = 1
        for i in range(1, len(S)+1):
            for j in range(1, len(T)+1):
                if S[i-1] == T[j-1]:
                    DT[i][j] = DT[i-1][j-1] + DT[i-1][j]
                else:
                    DT[i][j] = DT[i-1][j]
        return DT[len(S)][len(T)]
