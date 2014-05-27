"""
From: https://oj.leetcode.com/problems/count-and-say/
Author: Jing Zhou
Date: May 26, 2014
Thought: Quite easy... just a nested looping
"""



class Solution:
    # @return a string
    def countAndSay(self, n):
        s = '1'
        for i in range(1, n):
            newS = ''
            num = 1
            for j in range(len(s)):
                if j == len(s)-1:
                    newS += str(num)+s[-1]
                elif s[j] == s[j+1]:
                    num += 1
                else:
                    newS += str(num) + s[j]
                    num = 1
            s = newS
        return s
