#!/usr/bin/env python
# encoding: utf-8
import itertools

class Solution:
    def __init__(self):
        self.li = []

    def subsetsWithDup(self, S):
        n = len(S)
        res = []
        self.solve(res, 0, n)

        li_set = set(tuple(x) for x in self.li)
        l = [list(x) for x in li_set]
        l.sort(key = lambda x: self.li.index(x))
        return l

    def solve(self, res, pos, n):
        if pos == n:
            self.li.append(list(res))
            return

        self.solve(res, pos+1, n)
        res.append(S[pos])
        self.solve(res, pos+1, n)
        res.pop()

if __name__ == "__main__":
    s = Solution()
    S = [4,1,0]
    print(s.subsetsWithDup(S))
