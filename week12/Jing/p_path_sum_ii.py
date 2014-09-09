"""
From: https://oj.leetcode.com/problems/path-sum-ii/
Author: Jing Zhou
Date: May 30, 2014
Thought: Path sum II, python got TLE
"""



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if not root:
            return []
        result = []
        self.path(root, [], sum, result)
        return result
    def path(self, node, l, summ, result):
        if node.val == summ and node.left is None and node.right is None:
            l.append(node.val)
            result.append(l)
            return
        if summ < 0:
            return
        l.append(node.val)
        if node.left:
            self.path(node.left, l, summ - node.val, result)
        if node.right:
            self.path(node.right, l, summ - node.val, result)
