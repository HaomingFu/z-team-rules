"""
From: https://oj.leetcode.com/problems/divide-two-integers/
Author: Jing Zhou
Date: Jun 04, 2014
Thought: I used mutiplication after all... But not in the core algorithm. The core idea is use shift and |
"""



class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        sign1 = 1 if dividend > 0 else -1
        sign2 = 1 if divisor > 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if divisor > dividend:
            return 0
        if divisor == dividend:
            return 1*sign1*sign2
        denom = divisor
        current = 1
        answer = 0
        while(dividend >> 1 >= denom):
            denom <<= 1
            current <<= 1

        while current != 0:
            if dividend >= denom:
                dividend -= denom
                answer |= current
            denom >>= 1
            current >>= 1
        return answer*sign1*sign2
