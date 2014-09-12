"""
From: https://oj.leetcode.com/problems/unique-binary-search-trees-ii/
Author: Jing Zhou
Date: Sep 11, 2014
Thought: recursion again, consider every node to be the root then construct the tree
Tags: recusion, tree, BT
"""



class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self.generate(1, n)

    def generate(self, start, end):
        res = []
        if start > end:
            res.append(None)
            return res
        for i in range(start, end+1):
            leftNodes = self.generate(start, i-1)
            rightNodes = self.generate(i+1, end)

            for left in leftNodes:
                for right in rightNodes:
                    node = TreeNode(i)
                    node.left = left
                    node.right = right
                    res.append(node)
        return res
