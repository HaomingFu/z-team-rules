#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def subset(self, s):
        n = len(s)
        if n < 1:
            return [[]]
        s.sort()
        res = []
        self.solve(s, 0, n, [], res)
        return res

    def solve(self, s, ix, n, tmp, res):
        if ix==n:
            res.append(list(tmp))
            return

        tmp.append(s[ix])
        self.solve(s, ix+1, n, tmp, res)
        tmp.pop()
        self.solve(s, ix+1, n, tmp, res)



s = [4, 1, 0]
S = Solution()
print(S.subset(s))
