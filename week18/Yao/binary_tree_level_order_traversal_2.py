#!/usr/bin/env python
# encoding: utf-8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if not root:
            return []
        level = [root]
        stack = []
        res = []
        while level:
            stack.append(level)
            childs = []
            for node in level:
                if node.left:
                    childs.append(node.left)
                if node.right:
                    childs.append(node.right)
            level = childs
        while stack:
            level = stack.pop()
            val = []
            for node in level:
                val.append(node.val)
            res.append(val)
        return res
