#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/maximum-depth-of-binary-tree/
# Date: Sep. 9, 2014
# Status: AC

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1
