"""
From: https://oj.leetcode.com/problems/flatten-binary-tree-to-linked-list/
Author: Jing Zhou
Date: Jun 03, 2014
Thought: Recursion seems to be a good idea but no recursion also works.
"""



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        while root:
            if root.left:
                node = root.left
                while node.right:
                    node = node.right
                node.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
