"""
From: https://oj.leetcode.com/problems/search-in-rotated-sorted-array/
Author: Jing Zhou
Date: Sep 04, 2014
Thought: Not hard, yet I forgot the equal cases every time...
Tags: BS, tree, array, search
"""



class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        N = len(A)
        left, right = 0, N-1
        while left <= right:
            mid = (left+right)/2
            if A[mid] == target:
                return mid
            if A[mid] >= A[left]:
                if A[mid] > target and A[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if A[mid] < target and A[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
