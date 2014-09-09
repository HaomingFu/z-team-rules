#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Status: Accepted
# Date: Sep. 9, 2014

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num) < 1:
            return None
        if len(num) == 1:
            return TreeNode(num[0])

        mid  = int(len(num)/2)
        root = TreeNode(num[mid])
        left = num[0:mid]
        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(num[mid+1:])
        return root
