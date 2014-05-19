"""
From: http://oj.leetcode.com/problems/gas-station/
Author: Jing Zhou
Date: May 19, 2014
Thought: The idea of diff should come up easier but the observation about what can be valid starting point candidate... is not so easy
Not quite convinced also... will review soon
"""



class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        diff = [gas[i]-cost[i] for i in range(len(gas))]
        i = sumDiff = 0
        if sum(diff) < 0:
            return -1
        index = 0
        while i < len(gas):
            sumDiff = sumDiff + diff[i]
            if sumDiff < 0:
                sumDiff = 0
                index = i + 1
            i += 1
        return index
