"""
From: https://oj.leetcode.com/problems/plus-one/
Author: Jing Zhou
Date: May 26, 2014
Thought: EASYYYY
"""



class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        place = 0
        digits[-1] = digits[-1]+1
        if digits[-1] >= 10:
            digits[-1] = digits[-1]-10
            place = 1
        for i in range(len(digits)-2, -1, -1):
            if digits[i] + place >= 10:
                digits[i] = digits[i] + place - 10
                place = 1
            else:
                digits[i] = digits[i] + place
                place = 0
        if place == 1:
            digits.insert(0, 1)
        return digits
