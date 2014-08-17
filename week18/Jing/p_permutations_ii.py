"""
From: https://oj.leetcode.com/problems/permutations-ii/
Author: Jing Zhou
Date: Jul 21, 2014
Thought: Same sort of recursion with a lot of problems
Tags: permutation, recursion
"""



class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        result, solution = [], []
        visited = [0]*len(num)
        num.sort()
        self.generatePerm(num, 0, result, solution, visited)
        return result

    def generatePerm(self, num, step, result, solution, visited):
        if step == len(num):
            result.append(solution[::])
            return
        for i in range(0, len(num)):
            if visited[i] == 0:
                if i > 0 and num[i] == num[i-1] and visited[i-1] == 0:
                    continue
                visited[i] = 1
                solution.append(num[i])
                self.generatePerm(num, step+1, result, solution, visited)
                solution.pop()
                visited[i] = 0
