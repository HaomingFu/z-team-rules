#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/submissions/detail/11390588/
# Status: AC
# Date: Sep. 14, 2014

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # @param root, a tree node
    # @return boolean
    def isValidBST(self, root):
        if not root:
            return True
        stackNode = []
        val = []
        curNode = root
        while stackNode or curNode:
            if curNode:
                stackNode.append(curNode)
                curNode= curNode.left
            else:
                curNode = stackNode.pop()
                val.append(curNode.val)
                curNode = curNode.right
        num = len(val)
        if num==1:
            return True
        for i in range(1, num):
            if val[i-1]>= val[i]:
                return False
        return True
