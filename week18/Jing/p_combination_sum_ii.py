"""
From: https://oj.leetcode.com/problems/combination-sum-ii/
Author: Jing Zhou
Date: Jul 20, 2014
Thought: the difference is to remove duplication. Note this exceed the time limit...
Tags: recursion, combination, sum
"""



class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        result = []
        solution = []
        candidates.sort()
        self.addCombinationSum(candidates, target, total, result, solution)
        return result

    def addCombinationSum(self, candidates, target, depth, result, solution):
        if total > target or depth >= len(candidates):
            return
        if total == target:
            result.append(solution[::])
            return
        for i in range(depth, len(candidates)):
            if i > depth and candidates[i] == candidates[i-1]:
                continue
            total += candidates[i]
            solution.append(candidates[i])
            self.addCombinationSum(candidates, target-candidates[i], i+1, result, solution)
            solution.pop()
            total -= candidates[i]

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        result = []
        solution = []
        candidates.sort()
        self.addCombinationSum(candidates, target, 0, result, solution)
        return result

    def addCombinationSum(self, candidates, target, depth, result, solution):
        if target == 0:
            result.append(solution[::])
            return
        if target < 0 or depth >= len(candidates):
            return
        for i in range(depth, len(candidates)):
            if i > depth and candidates[i] == candidates[i-1]:
                continue
            solution.append(candidates[i])
            self.addCombinationSum(candidates, target-candidates[i], i+1, result, solution)
            solution.pop()
