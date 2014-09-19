"""
From: https://oj.leetcode.com/problems/4sum/
Author: Jing Zhou
Date: Sep 13, 2014
Thought: the use of hash is important
Tags: hash, dictionary, map, sum, k sum
"""



class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        nums = sorted(num)
        result = set()
        cache  = collections.defaultdict(set)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for half in cache[target - nums[i] - nums[j]]:
                    result.add(tuple(list(half) + [nums[i], nums[j]]))

            for j in range(i):
                cache[nums[i] + nums[j]].add((nums[j], nums[i]))

        return map(list, result)
