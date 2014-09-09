"""
From: https://oj.leetcode.com/problems/integer-to-roman/
Author: Jing Zhou
Date: Jun 05, 2014
Thought: Good to know the function divmod... which is super handy to use
Algorthm from: http://rosettacode.org/wiki/Roman_numerals/Encode#Python
"""



iclass Solution:
    # @return a string
    def intToRoman(self, num):
        res = []
        anums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        rnums = "M CM D CD C XC L XL X IX V IV I".split()
        for a, r in zip(anums, rnums):
            n, num = divmod(num, a)
            res.append(r*n)
        return ''.join(res)
