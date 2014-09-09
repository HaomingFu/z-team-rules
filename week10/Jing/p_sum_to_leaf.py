"""
From: http://oj.leetcode.com/problems/sum-root-to-leaf-numbers/
Author: Jing Zhou
Date: May 18, 2014
Thought: recursion again. Not very hard.
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
    def sumNumbers(self, root):
        return self.sumIt(root, 0)

    def sumIt(self, root, num):
        if not root:
            return 0
        num = num*10 + root.val
        if not root.left and not root.right:
            return num
        else:
            return self.sumIt(root.left, num) + self.sumIt(root.right, num)


