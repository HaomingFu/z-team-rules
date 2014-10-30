#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def numDecodings(self, s):
        n = len(s)
        res = [1]*n
        if n < 1:
            return 0
        if s[0]=='0':
            return 0
        if n > 1:
            if s[1] =='0' and int(s[0:2]) not in range(1, 27):
                return 0
            if int(s[0:2]) in range(1, 27) and s[1]!='0':
                res[1] = 2
            else:
                res[1]= 1
            for i in range(2, n):
                if s[i]=='0':
                    if not int(s[i-1:i+1]) in range(1, 27):
                        return 0
                    res[i] = res[i-2]
                elif int(s[i-1:i+1]) in range(1, 27) and s[i-1]!='0':
                    res[i] = res[i-1] + res[i-2]
                else:
                    res[i] = res[i-1]

        return res[-1]


nums = '30'
s = Solution()
print(s.numDecodings(nums))
