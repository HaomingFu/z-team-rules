"""
From: https://oj.leetcode.com/problems/next-permutation/
Author: Jing Zhou
Date: Aug 18, 2014
Thought: Next permutation using the algorithm in C++ New solution that's inspired by reading up permutation. The old solution is kinda crappy.
Tags: permutation
"""



class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if not num:
            return num
        for j in range(len(num)-1, -1, -1):
            if j-1>=0 and num[j-1]<num[j]:
                break
        if j == 0:
            num.reverse()
            return num
        j -= 1
        for m in range(len(num)-1, j, -1):
            if num[m] > num[j]:
                num[m], num[j] = num[j], num[m]
                break
        # Note here the reverse can be written(should be wriiten into a function since
        # the problem states no extra space...
        num = num[:j+1] + list(reversed(num[j+1:]))
        return num
