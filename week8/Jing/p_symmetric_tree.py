"""
From: http://oj.leetcode.com/problems/symmetric-tree/
Author: Jing Zhou
Date: May 1, 2014
Thought: recursively solve the problem is very easy...
I think I'll rewrite all of them into iterative solutions
one day...
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
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isSym(root.left, root.right)
    def isSym(self, left, right):
        if not left and not right:
            return True
        if left and right:
            if left.val == right.val:
                return self.isSym(left.left, right.right) and self.isSym(left.right, right.left)
            return False
        return False
