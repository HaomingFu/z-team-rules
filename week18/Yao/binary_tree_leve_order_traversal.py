#!/usr/bin/env python
# encoding: utf-8

#From: https://oj.leetcode.com/problems/binary-tree-level-order-traversal/
#Date: September 2
#Status: Accepted

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if not root:
            return []
        level = [root]
        res = []
        while level:
            vals = []
            childs = []
            for node in level:
                vals.append(node.val)
                if node.left:
                    childs.append(node.left)
                if node.right:
                    childs.append(node.right)
            res.append(vals)
            level = childs
        return res
