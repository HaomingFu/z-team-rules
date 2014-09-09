"""
From: http://oj.leetcode.com/problems/validate-binary-search-tree/
Author: Jing Zhou
Date: April 28, 2014
Thought: the use of 1000000.. is not very ideal.
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
    def isValidBST(self, root):
        return self.helpValid(root, 10000000, -10000000)
    
    def helpValid(self, root, maxN, minN):
        if not root:
            return True
        if root.left and (root.left.val <= minN or root.left.val >= root.val):
            return False
        if root.right and (root.right.val >= maxN or root.right.val <= root.val):
            return False
        return self.helpValid(root.left, root.val, minN) and self.helpValid(root.right, maxN, root.val)
