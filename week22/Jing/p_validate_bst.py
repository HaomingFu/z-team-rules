"""
From: https://oj.leetcode.com/problems/validate-binary-search-tree/
Author: Jing Zhou
Date: Sep 01, 2014
Thought: New solution for an old problem. This one use compare pre with the node.
The use of list...
Tags: BST, tree, recursion
"""




class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        if not root:
            return True
        prev = [-100000]
        return self.validate(root, prev)

    def validate(self, root, prev):
        if not root:
            return True
        if self.validate(root.left, prev):
            if root.val > prev[0]:
                prev[0] = root.val
                return self.validate(root.right, prev)
            else:
                return False
        else:
            return False
