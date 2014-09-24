#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/recover-binary-search-tree/
# Status: AC
# Date: Sep. 16, 2014

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        if not root:
            return root
        stackNode = []
        stackVal = []
        nodeList = []
        curNode = root
        while curNode or stackNode:
            if curNode:
                stackNode.append(curNode)
                curNode = curNode.left
            else:
                curNode = stackNode.pop()
                nodeList .append(curNode)
                stackVal .append(curNode.val)
                curNode = curNode.right
        stackVal.sort()
        num = len(stackVal)
        for ix in range(0, num):
            nodeList[ix].val = stackVal[ix]
        return root
