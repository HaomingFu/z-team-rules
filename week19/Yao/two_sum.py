# From: https://oj.leetcode.com/problems/two-sum/
# Status: Accepted
# Date: August 4

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        n = len(num)
        map = dict()
        for i in range(0, n):
            if target-num[i] in map:
                return (map[target-num[i]], i+1)
            else:
                map[num[i]] = i + 1
