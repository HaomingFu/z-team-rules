"""
From: http://oj.leetcode.com/problems/binary-tree-postorder-traversal/
Author: Jing Zhou
Date: April 21, 2014
Complexity: O(n)
Hardness: super easy(with recursion)
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
    def postorderTraversal(self, root):
        self.result = []
        self.postorder(root)
        return self.result

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.result.append(root.val)
