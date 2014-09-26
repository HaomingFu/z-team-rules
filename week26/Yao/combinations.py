#!/usr/bin/env python
# encoding: utf-8
# From:https://oj.leetcode.com/problems/combinations/
# Status: AC
# Date: Sep. 26, 2014
class Solution:
    def combine(self, n, k):
        res = []
        if k ==1:
            for x in range(1, n+1):
                res.append([x])
            return res
        if n == 1:
            return [[n]]
        if n == k:
            return [[ix for ix in range(1, n+1)]]
        res1 = self.combine(n-1, k)
        res2 = self.combine(n-1, k-1)
        for i in res2:
            i.append(n)
        return res1 + res2

if __name__ == "__main__":
    s = Solution()
    print(s.combine(4,3))
