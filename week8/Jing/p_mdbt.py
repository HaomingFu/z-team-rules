"""
From: http://oj.leetcode.com/problems/minimum-depth-of-binary-tree/
Author: Jing Zhou
Date: April 29, 2014
Though: think it through...
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
    def minDepth(self, root):
        return self.depth(root, 0)
    def depth(self, root, d):
        if not root:
            return d
        d += 1
        if root.left and root.right:
            return min(self.depth(root.left, d), self.depth(root.right, d))
        if root.left:
            return self.depth(root.left, d)
        if root.right:
            return self.depth(root.right, d)
        return d
