#!/usr/bin/env python
# encoding: utf-8

# From:https://oj.leetcode.com/problems/minimum-depth-of-binary-tree/
# Status: Accepted
# Date: Sep. 9, 2014

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # return an integer
    def minDepth(self, root):
        if not root:
            return 0
        hl = self.minDepth(root.left)
        hr = self.minDepth(root.right)
        if hl > 0 and hr > 0 :
            return min(h1, hr) + 1
        else:
            return max(h1, hr) + 1
