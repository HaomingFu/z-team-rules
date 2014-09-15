#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Status: AC
# Date: Sep. 15

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root:
            curNode = root
            stackNode = []
            val = []
            while curNode or stackNode:
                if curNode:
                    val.append(curNode)
                    stackNode.append(curNode)
                    curNode = curNode.left
                else:
                    curNode = stackNode.pop()
                    curNode = curNode.right
            curNode = root
            curNode.left = None
            for node in val[1:]:
                node.left = None
                curNode.right = node
                curNode = node

