#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/unique-binary-search-trees-ii/
# Status: AC
# Date: Sep. 14

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param n, an integer
    # @return a list of tree node
    def generateTrees(self, n):

        return self.genTrees(1, n)

    def genTrees(self, start, end):
        trees = []
        if start > end:
            trees.append(None)
            return trees
        if start == end:
            trees.append(TreeNode(start))
            return trees

        for ix in range(start, end+1):
            left = genTrees(start, ix-1)
            right = genTrees(ix, end)
            for lnode in left:
                for rnode in right:
                    root = TreeNode(ix)
                    root.left = lnode
                    root.right = rnode
                    trees.append(root)
        return trees
