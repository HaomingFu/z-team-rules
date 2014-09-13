#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/sum-root-to-leaf-numbers/
# Status: AC
# Date: Sep. 13, 2014

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree none
    # @return an integer
    def sumNumber(self, root):
        if not root:
            return 0
        sum = 0
        curNode = root
        curVal = root.val
        nodeStack = []
        valStack = []
        while nodeStack or curNode:
            if curNode:
                nodeStack.append(curNode)
                valStack.append(curVal)
                curNode = curNode.left
                if curNode:
                    curVal = 10*curVal + curNode.val
            else:
                curNode = nodeStack.pop()
                curVal = valStack.pop()
                curNode = curNode.right
                if curNode:
                    curVal = 10*curVal + curNode.val
                elif not curNode.left:
                    sum = sum + curVal
            return sum
