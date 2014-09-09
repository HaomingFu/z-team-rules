"""
From: https://oj.leetcode.com/problems/recover-binary-search-tree/
Author: Jing Zhou
Date: Sep 01, 2014
Thought: used the same method to traverse the tree in order, then find the abnormal nodes
Tags: BST, tree, recursion
"""



class Solution:
    # @param root, a tree node
    # @return a tree node
    def __init__(self):
        """ Okay I did so many problems now and I
        """
        self.first = None
        self.second = None
        self.pre = None
    def recoverTree(self, root):
        if not root:
            return root
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        return root
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if not self.pre:
            self.pre = root
        else:
            if self.pre.val > root.val:
                if not self.first:
                    self.first = self.pre
                self.second = root
            self.pre = root
        self.inorder(root.right)
