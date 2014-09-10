"""
From: https://oj.leetcode.com/problems/search-for-a-range/
Author: Jing Zhou
Date: Sep 06, 2014
Thought: About as the same as binary search but here you the termination condition is left and right elements equal to the target value
Tags: BS, array
"""



class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        left, right = 0, len(A)-1
        while left <= right:
            if A[left] == target and A[right] == target:
                return [left, right]
            mid = (left+right)/2
            if A[mid] > target:
                right = mid - 1
            elif A[mid] < target:
                left = mid + 1
            else:
                while A[left] < target:
                    left += 1
                while A[right] > target:
                    right -= 1
        return [-1, -1]
