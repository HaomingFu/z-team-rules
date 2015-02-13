#!/usr/bin/env python
# encoding: utf-8

class Interval:
    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e
class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals
        intervals = sorted(intervals, self.sortFunc)
        res = []
        temp = []
        for ix in range(0, len(intervals)):
            if not temp:
                temp = intervals[ix]
                continue
            elif intervals[ix].start <= temp.end:
                temp.end= max(temp.end, intervals[ix].end)
            else:
                res.append(temp)
                temp = intervals[ix]
        res.append(temp)
        return res


    def sortFunc(self, a, b):
        if a.start > b.start:
            return 1
        if a.start < b.start:
            return -1
        return 0


s = Solution()
intervals = [Interval(1, 5), Interval(1,5)]

res = s.merge(intervals)
for ix in res:
    print(ix.start, ix.end)
