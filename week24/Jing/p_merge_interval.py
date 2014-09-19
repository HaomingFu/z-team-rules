"""
From: https://oj.leetcode.com/problems/merge-intervals/
Author: Jing Zhou
Date: Sep 12, 2014
Thought: Sort then merge, easy
Tags: sort, list, sorted
"""



# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if not intervals or len(intervals) == 1:
            return intervals
        # or use key = lambda x: x.start
        intervals = sorted(intervals, key=operator.attrgetter('start'))
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i].start <= res[-1].end:
                res[-1].end = max(res[-1].end, intervals[i].end)
            else:
                res.append(intervals[i])
        return res
