#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        n = len(candidates)
        if n<1:
            return []

        res = []
        self.solve(candidates, target, [], 0, n, res)


        return res

    def solve(self, candidates, target, li, ix, n, res):
        if target==0:
            res.append(list(li))
            return
        if ix ==n or target<0:
            return
        li.append(candidates[ix])
        self.solve(candidates, target-candidates[ix], li, ix+1, n, res)
        li.pop()
        jx = ix +1
        while jx < n and candidates[jx] == candidates[jx-1]:
            jx += 1
        self.solve(candidates, target, li, jx, n, res)


s = Solution()
print(s.combinationSum2([10], 1))
