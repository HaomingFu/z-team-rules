"""
From: http://oj.leetcode.com/problems/balanced-binary-tree/
Author: Jing Zhou
Date: April 30, 2014
Thought:
"""
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if not root:
            return True
        return True if self.height(root) else False
    def height(self, node):
        if not node:
            return 0
        hl = self.height(node.left)
        if hl is False:
            return False
        hr = self.height(node.right)
        if hr is False:
            return False
        if abs(hr-hl) >1:
            return False
        return max(hr, hl)+1
