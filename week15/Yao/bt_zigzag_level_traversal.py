#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Date: Sep. 9,
# Status: AC

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = []
        level = [root]
        reverse = True
        while level:
            child = []
            val = []
            reverse = not reverse
            for node in level:
                val.append(node.val)
            if reverse:
                val.reverse()
            res.append(val)
            for node in level:
                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)
            level = child
        return res


