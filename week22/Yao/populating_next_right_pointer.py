#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node/
# Date: Setember 2
# Status: Accepted
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root:
            level = [root]
            while level :
                childs = []
                num = len(level)
                for ix in range(0, num-1):
                    level[ix].next = level[ix+1]
                    if level[ix].left:
                        childs.append(level[ix].left)
                    if level[ix].right:
                        childs.append(level[ix].right)
                if level[num-1].left:
                    childs.append(level[num-1].left)
                if level[num-1].right:
                    childs.append(level[num-1].right)
