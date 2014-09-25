#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/path-sum-ii/
# Status: AC
# Date: Sep. 25

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        li = self.returnPath(root, sum)
        res = []
        if li:
            for i in li:
                i.reverse()
                res.append(i)
        return res

    def returnPath(self, root, sum):
        if not root:
            return []
        if not root.left and not root.right:
            if root.val==sum:
                return [[root.val]]
            else:
                return []
        left = self.returnPath(root.left, sum-root.val)
        right = self.returnPath(root.right, sum-root.val)
        res = []
        if left:
            for i in left:
                i.append(root.val)
                res.append(i)
        if right:
            for i in right:
                i.append(root.val)
                res.append(i)
        return res
if __name__ == "__main__":
    root = TreeNode(8)
    s = Solution()
    print(s.pathSum(root, 8))
