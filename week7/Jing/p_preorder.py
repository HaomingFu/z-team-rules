"""
From: http://oj.leetcode.com/problems/binary-tree-preorder-traversal/
Author: Jing Zhou
Date: April 21, 2014
Complexity: O(n)
Hardness: super easy
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        self.result = []
        self.preorder(root)
        return self.result

    def preorder(self, root):
        if root:
            self.result.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)
