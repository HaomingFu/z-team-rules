#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        maxLen = 1
        for ix in range(0, len(s)-1):
            for j in range(2):
                if j == 0:
                    back = ix
                    forward = ix + 1
                else:
                    back = ix - 1
                    forward = ix + 1
                while back >= 0 and forward < len(s):
                    if s[back] == s[forward]:
                        back -= 1
                        forward += 1
                    else:
                        break
                dist = forward - back - 1
                if maxLen < dist:
                    maxLen = dist
                    maxStr = s[(back+1):forward]
        return maxStr

ans = Solution()
s = 'cccc'
print(ans.longestPalindrome(s))
