#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/path-sum/
# Status: Accepted
# Date: Sep. 9, 2014
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # return a boolean
    def hasPathSum(self, root, sum):
        if not root:
            return false
        if not root.left and not root.right:
            return root.val == sum
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

