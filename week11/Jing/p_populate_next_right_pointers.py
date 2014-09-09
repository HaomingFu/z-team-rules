"""
From: https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node/
Author: Jing Zhou
Date: May 23, 2014
Thought: Initially I thought I could use BFS but it turns out I neglected the fact that the next pointer can be used right away once created. Dynamic view needed
"""



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        if root.left:
            root.left.next = root.right
        if root.right:
            root.right.next = root.next.left if root.next else None
        self.connect(root.left)
        self.connect(root.right)
