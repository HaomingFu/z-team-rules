"""
From: https://oj.leetcode.com/problems/permutation-sequence/
Author: Jing Zhou
Date: Jul 30, 2014
Thought: Basically a math problem. Think it through and it's super easy
Tags: math, permutation, numbers
"""



class Solution:
    # @return a string
    def getPermutation(self, n, k):
        numbers = [i for i in range(1, (n+1))]
        factorial = math.factorial(n)
        k -= 1

        result = ""
        for i in range(n):
            factorial = factorial/(n-i)
            cur = k/factorial

            k = k % factorial
            result += str(numbers[cur])
            numbers.remove(numbers[cur])
        return result
