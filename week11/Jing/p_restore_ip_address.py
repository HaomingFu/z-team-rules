"""
From: https://oj.leetcode.com/problems/restore-ip-addresses/
Author: Jing Zhou
Date: May 21, 2014
Thought: Used 3 for loops not a very neat solution but it worked
"""



class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        if len(s) < 4 or len(s) > 12:
            return []
        result = []
        for i in range(1, len(s)-2):
            for j in range(i+1, len(s)):
                for k in range(j+1, len(s)):
                    if int(s[:i]) < 256 and int(s[i:j]) < 256 and int(s[j:k]) < 256 and int(s[k:]) < 256:
                        if i>=2 and s[:i].startswith('0') or j-i>=2 and s[i:j].startswith('0') or k-j>=2 and s[j:k].startswith('0') or len(s)-k>=2 and s[k:].startswith('0'):
                            continue
                        result.append(s[:i]+"."+s[i:j]+"."+s[j:k]+"."+s[k:])
        return result
