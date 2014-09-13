#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/sum-root-to-leaf-numbers/
# Status: Accepted
# Date: Sep. 13, 2014

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if not root:
            return 0
        sum = 0
        nodes = [root]
        vals = [root.val]
        while nodes:
            childNodes = []
            childVals = []
            for i in range(0, len(nodes)):
                p = nodes[i]
                if p.left:
                    childNodes.append(p.left)
                    childVals.append(p.left.val + 10*(vals[i]))
                if p.right:
                    childNodes.append(p.right)
                    childVals.append(p.right.val + 10*vals[i])
                if not p.left and not p.right:
                    sum = sum + vals[i]
            nodes = childNodes
            vals = childVals
        return sum
