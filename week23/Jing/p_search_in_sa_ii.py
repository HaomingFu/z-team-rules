"""
From: https://oj.leetcode.com/problems/search-in-rotated-sorted-array-ii/
Author: Jing Zhou
Date: Sep 04, 2014
Thought: things changed... there is o(n) worst case
Tags: BS, tree, array, search
"""



class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        N = len(A)
        left, right = 0, N-1
        while left <= right:
            mid = (left+right)/2
            if A[mid] == target:
                return True
            if A[mid] > A[left]:
                if A[mid] > target and A[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            elif A[mid] < A[left]:
                if A[mid] < target and A[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
            #if A[mid] == A[left], just increase left by one and see what happens
                left += 1
        return False
