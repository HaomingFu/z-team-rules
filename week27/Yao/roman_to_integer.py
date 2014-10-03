#!/usr/bin/env python
# encoding: utf-8

# From:

class Solution:
    # @return an integer
    def romanToInt(self, s):
        maps = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        n = len(s)
        if n < 1:
            return 0
        if n == 1:
            return maps[s[0]]
        for i in range(0, n-1):
            c = s[i]
            cn = s[i+1]
            if maps[c] <  maps[cn]:
                res -= maps[c]
            else:
                res += maps[c]
        c = s[n-1]
        res += maps[c]

        return res

if __name__ == "__main__":
    s = Solution()
    roman = "MMMCMXCIX"
    print(s.romanToInt(roman))
