#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/same-tree/
# Status: Accepted
# Date: Sep. 9, 2014

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @ return a boolean
    def isSameTree(self, p, q):
        if not p or not q:
            return not p and not q
        return p.val == q.val and \
                self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
