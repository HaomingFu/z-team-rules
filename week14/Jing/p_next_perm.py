"""
From: https://oj.leetcode.com/problems/next-permutation/
Author: Jing Zhou
Date: Jun 15, 2014
Thought: The general idea is not hard to think of. The use of a dictionary is really helpful.
"""



class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if not num:
            return num
        minDict = {}
        maxN, minN = -1, 11
        found = False
        for j in range(len(num)-1, -1, -1):
            if num[j] not in minDict:
                minDict[num[j]] = j
                if num[j] > maxN:
                    maxN = num[j]
                elif num[j] < minN:
                    minN = num[j]
            if num[j] < maxN:
                found = True
                break
        if found:
            for i in range(num[j]+1, maxN+1):
                if i in minDict:
                    num[j], num[minDict[i]] = i, num[j]
                    num[j+1:] = sorted(num[j+1:])
                    return num
        num.reverse()
        return num
