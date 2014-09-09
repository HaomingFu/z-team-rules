#!/usr/bin/env python
# encoding: utf-8

#From: https://oj.leetcode.com/problems/binary-tree-inorder-traversal/
#Status: Accepted
#Date: August 31
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        iter = root
        stack = []
        res = []
        while iter or stack:
            if iter:
                stack.append(iter)
                iter = iter.left
            else:
                iter = stack.pop()
                res.append(iter.val)
                iter = iter.right
        return res


