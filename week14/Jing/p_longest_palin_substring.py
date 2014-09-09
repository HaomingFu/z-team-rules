"""
From: https://oj.leetcode.com/problems/longest-palindromic-substring/
Author: Jing Zhou
Date: Jun 15, 2014
Thought: too much details that need to be aware of. But the basic idea behind it is straightforward.
"""



class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if not s:
            return s
        if len(s) == 1 or len(s) == 2 and s[0] == s[1]:
            return s
        left, right = 0, 0
        maxL = 1
        for i in range(len(s)):
            l = 1
            for j in range(1, i+1):
                if i+j < len(s) and s[i-j] == s[i+j]:
                    l += 2
                    if i-j == 0:
                        if l > maxL:
                            maxL = l
                            left, right = i-j, i+j+1
                            if i+j == len(s)-1:
                                return s
                else:
                    if l > maxL:
                        maxL = l
                        left, right = i-j+1, i+j
                    break
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                l = 2
                for j in range(1, i+1):
                    if i+j+1 < len(s) and s[i-j] == s[i+j+1]:
                        l += 2
                        if i-j == 0:
                            if l > maxL:
                                maxL = l
                                left, right = i-j, i+j+2
                                if i+j+1 == len(s)-1:
                                    return s
                    else:
                        if l > maxL:
                            maxL = l
                            left, right = i-j+1, i+j+1
                        break
                if l == 2 and l > maxL:
                    maxL = 2
                    left, right = i, i+2
        return s[left:right]
