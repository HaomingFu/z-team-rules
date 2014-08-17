"""
From: https://oj.leetcode.com/problems/combination-sum/
Author: Jing Zhou
Date: Jul 20, 2014
Thought: Similar to permutation problem
Tags: recursion, combination, sum
"""



class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        result = []
        solution = []
        total = 0
        candidates.sort()
        self.addCombinationSum(candidates, target, 0, total, result, solution)
        return result

    def addCombinationSum(self, candidates, target, depth, total, result, solution):
        if total > target:
            return
        if total == target:
            result.append(solution[:])
            return
        for i in range(depth, len(candidates)):
            total += candidates[i]
            solution.append(candidates[i])
            self.addCombinationSum(candidates, target, i, total, result, solution)
            solution.pop()
            total -= candidates[i]
