"""
From: https://oj.leetcode.com/problems/binary-tree-maximum-path-sum/
Author: Jing Zhou
Date: Jun 03, 2014
Thought: This one is quite interesting... A list is passed. Then there are several cases to consider. Especially the difference of passing a node or making the node the root.
"""



class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        max_v = [-999]
        self.getMax(root, max_v)
        return max_v[0]
    def getMax(self, root, max_v):
        if not root:
            return 0
        l = self.getMax(root.left, max_v)
        r = self.getMax(root.right, max_v)
        m = root.val
        arch = l+r+m
        crossRoot = max(max(l, r)+m, m)
        max_v[0] = max(max_v[0], arch, crossRoot)
        return crossRoot
