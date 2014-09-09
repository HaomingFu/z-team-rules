"""
From: http://oj.leetcode.com/problems/path-sum/
Author: Jing Zhou
Date: May 3, 2014
Thought: Mistake 1: thought sum was positive...Mistake 2:
not to leaf...
"""
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        return self.getSum(root, sum)
    def getSum(self, node, left):
        if not node:
            return False
        if not node.left and not node.right and left == node.val:
            return True
        return self.getSum(node.left, left-node.val) or self.getSum(node.right, left-node.val)
