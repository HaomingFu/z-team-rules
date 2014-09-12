"""
From: https://oj.leetcode.com/problems/decode-ways/
Author: Jing Zhou
Date: Sep 11, 2014
Thought: dynamic programming. but be aware of 0. it's tricky there
Tags: DP, dynamic programming, details
"""



class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        """
        if len(s) <= 1:
            return 1
        for char in s:
            if char=="1" or char=="2" and int(char) <=6:
                return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        return 1
        """
        if not s:
            return 0
        res = [1]*(len(s)+1)
        for i, char in enumerate(s):
            if i == 0 and char == "0":
                return 0
            if i >=1:
                if s[i-1] == "1" and int(char) > 0 or s[i-1] == "2" and 0 < int(char) <= 6:
                    res[i+1] = res[i] + res[i-1]
                elif (s[i-1] == "1" or s[i-1] == "2") and int(char) == 0:
                    res[i+1] = res[i-1]
                elif char == "0" and int(s[i-1]) not in [1,2]:
                    return 0
                else:
                    res[i+1] = res[i]
        return res[len(s)]
