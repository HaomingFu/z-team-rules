"""
From: https://oj.leetcode.com/problems/insert-interval/
Author: Jing Zhou
Date: Sep 12, 2014
Thought: The same with the last one, quite easy
Tags: sort, interval, list
"""



# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        return self.merge(intervals)

    def merge(self, intervals):
        if not intervals or len(intervals) == 1:
            return intervals
        intervals = sorted(intervals, key=operator.attrgetter('start'))
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i].start <= res[-1].end:
                res[-1].end = max(res[-1].end, intervals[i].end)
            else:
                res.append(intervals[i])
        return res
