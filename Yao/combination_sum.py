#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def combinationSum(self, candidates, target):
        res=[]
        li = list(set(candidates))
        li.sort()
        tmp = []
        self.solve(li, target, tmp, 0, res)

        return res
    def solve(self, cand, t, tmp, k, res):
        if t ==0:
            res.append(list(tmp))
            return
        if cand[k] <= t:
            i = k
            while i < len(cand) and cand[i] <= t:
                tmp.append(cand[i])
                self.solve(cand, t-cand[i], tmp, i, res)
                tmp.pop()
                i += 1

s = Solution()
cand = [1]
target = 1
print(s.combinationSum(cand, target))


