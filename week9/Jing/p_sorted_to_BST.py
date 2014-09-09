"""
From: http://oj.leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Author: Jing Zhou
Date: May 7, 2014
Thought: simple recursive algorithm
"""
class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if not num:
            return None
        end = len(num) - 1
        return self.constructTree(num, 0, end)
    def constructTree(self, array, start, end):
        if start > end:
            return None
        mid = (start + end)/2
        node = TreeNode(array[mid])
        node.left = self.constructTree(array, start, mid-1)
        node.right = self.constructTree(array, mid+1, end)
        return node
