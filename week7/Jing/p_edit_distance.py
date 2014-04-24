"""
From: http://oj.leetcode.com/problems/edit-distance/
Author: Jing Zhou
Date: April 23, 2014
Idea: basic dynamic programming
Complexity: O(mn), m and n is the length of two strings
"""

def minDistance(word1, word2):
    DP = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]
    for i in range(len(word1)+1):
        DP[0][i] = i
    for j in range(1, len(word2)+1):
        DP[j][0] = j
    for i in range(1, len(word1)+1):
        for j in range(1, len(word2)+1):
            DP[j][i] = min(DP[j-1][i]+1, DP[j][i-1]+1, DP[j-1][i-1] if word1[i-1]==word2[j-1] else DP[j-1][i-1]+1)
    return DP[len(word2)][len(word1)]
