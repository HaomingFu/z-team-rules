"""
From: http://oj.leetcode.com/problems/valid-parentheses/
Author: Jing Zhou
Date: April 30, 2014
Thought: easy, just need to use a stack. But make sure to check if it's
empty or not before popping.
"""
class Solution:
    # @return a boolean
    def isValid(self, s):
        d = collections.deque()
        for c in s:
            if c in set(['(', '{', '[']):
                d.append(c)
            else:
                if not d:
                    return False
                ch = d.pop()
                if c == ')' and ch != '(':
                    return False
                elif c == '}' and ch != '{':
                    return False
                elif c == ']' and ch != '[':
                    return False
        return True if not d else False
