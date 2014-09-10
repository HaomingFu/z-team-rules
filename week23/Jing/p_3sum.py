"""
From: https://oj.leetcode.com/problems/3sum/
Author: Jing Zhou
Date: Sep 06, 2014
Thought: first sort, then search
Tags: array, search
"""



class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if not num:
            return []
        res = []
        length = len(num)
        num.sort()
        for i, val in enumerate(num):
            if val <= 0 and i < length-2 and (i==0 or val > num[i-1]):
                left, right = i+1, length-1
                while left < right:
                    if num[left]+num[right] < -val:
                        left += 1
                    elif num[left]+num[right] > -val:
                        right -= 1
                    else:
                        res.append([val, num[left], num[right]])
                        left += 1
                        while num[left] == num[left-1] and left < right:
                            left += 1
                        right -= 1
                        while num[right] == num[right+1] and left < right:
                            right -= 1
        return res
