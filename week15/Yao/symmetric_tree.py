#!/usr/bin/env python
# encoding: utf-8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isSame(root.left, root.right)

    def isSame(self, lTree, rTree):
        if not lTree or not rTree:
            return not lTree and not rTree
        if lTree.val != rTree.val:
            return False
        else:
            return self.isSame(lTree.left, rTree.right) and \
                    self.isSame(lTree.right, rTree.left)
