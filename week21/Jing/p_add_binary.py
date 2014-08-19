"""
From: https://oj.leetcode.com/problems/add-binary/
Author: Jing Zhou
Date: Aug 19, 2014
Thought: Similar to the add two numbers problem
Tags: string
"""



class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        reversedA = a[::-1]
        reversedB = b[::-1]
        c = ""
        carry = 0
        while reversedA or reversedB:
            if reversedA:
                carry += int(reversedA[0])
                reversedA = reversedA[1:]
            if reversedB:
                carry += int(reversedB[0])
                reversedB = reversedB[1:]
            c += str(carry%2)
            carry = carry/2
        if carry:
            c += "1"
        return c[::-1]
