"""
From: http://oj.leetcode.com/discuss/oj/palindrome-number
Author: Jing Zhou
Date: April 20, 2014
Idea: just use division and modulo
"""

def isPalindrome(x):
    if x < 0:
        return False
    theSum = 0
    y = x
    while(y > 0):
        theSum = 10*theSum + y%10
        y = y/10
    return True if theSum == x else False
def test():
    print(isPalindrome(-10))

test()
