"""
From: https://oj.leetcode.com/problems/interleaving-string/
Author: Jing Zhou
Date: Sep 11, 2014
Thought: Dynamic programming. 2D. i, j
Tags: DP, dynamic programming, string
"""



class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        lenA, lenB, lenC = len(s1), len(s2), len(s3)
        if lenA + lenB != lenC:
            return False
        res = [[False]*(lenB+1) for _ in range(lenA+1)]
        for i in range(lenA+1):
            for j in range(lenB+1):
                if i == 0 and j == 0:
                    res[i][j] = True
                elif i == 0:
                    if s2[j-1] == s3[j-1]:
                        res[i][j] = res[i][j-1]
                elif j == 0:
                    if s1[i-1] == s3[i-1]:
                        res[i][j] = res[i-1][j]
                elif s3[i+j-1] == s1[i-1] and s3[i+j-1] != s2[j-1]:
                    res[i][j] = res[i-1][j]
                elif s3[i+j-1] == s2[j-1] and s3[i+j-1] != s1[i-1]:
                    res[i][j] = res[i][j-1]
                elif s3[i+j-1] == s2[j-1] and s3[i+j-1] == s1[i-1]:
                    res[i][j] = res[i-1][j] or res[i][j-1]
        return res[lenA][lenB]
