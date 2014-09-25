#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/palindrome-number/
# Date: Sep. 25, 2014
# Status:

class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        d = 1
        while x // (10*d):
            d *= 10
        while x > 0:
            first = x//d
            last = x % 10
            if first != last:
                return False
            x = x % d
            x = x // 10
            d = d/100
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(13231))

