#!/usr/bin/env python
# encoding: utf-8

# From:https://oj.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
# Status: Accepted
# Date: Sep. 9

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        num = []
        while head:
            num.append(head.val)
            head = head.next
        root = self.getTree(num)
        return root
    def getTree(self, num):
        if len(num) < 1:
            return None
        if len(num) == 1:
            return TreeNode(num[0])
        mid = int(len(num)/2)
        root = TreeNode(num[mid])
        root.left = self.getTree(num[0:mid])
        root.right = self.getTree(num[mid+1:])
        return root
