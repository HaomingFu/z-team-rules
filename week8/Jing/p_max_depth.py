"""
From: http://oj.leetcode.com/problems/maximum-depth-of-binary-tree/
Author: Jing Zhou
Date: May 4, 2014
Thought: Super easy...
"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
