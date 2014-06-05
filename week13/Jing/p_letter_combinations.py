"""
From: https://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/
Author: Jing Zhou
Date: Jun 04, 2014
Thought: This one is not hard... Just iteratively add one thing to the result
"""



class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        if not digits:
            return [""]
        res = [l for l in dic[digits[0]]]
        if len(digits) == 1:
            return res
        for i in range(1, len(digits)):
            newRes = [r+l for r in res for l in dic[digits[i]]]
            res = newRes
        return res
