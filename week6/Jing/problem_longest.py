"""
From: http://oj.leetcode.com/problems/longest-substring-without-repeating-characters/
Author: Jing Zhou
Date: April 15, 2014
Complexity: O(N), only go through the lsit once
Idea: keep two "pointers", used a set.
"""

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        sl = set()
        longest = 0
        length = 0
        i = 0
        for j in range(len(s)):
            if s[j] not in sl:
                sl.add(s[j])
                length = length + 1
            else:
                if length > longest:
                    longest = length
                while(s[i] != s[j]):
                    sl.remove(s[i])
                    i += 1
                i += 1
                length = j-i+1
 
        return length if length > longest else longest
