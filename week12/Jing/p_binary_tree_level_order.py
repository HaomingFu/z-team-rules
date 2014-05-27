"""
From: https://oj.leetcode.com/problems/binary-tree-level-order-traversal/
Author: Jing Zhou
Date: May 26, 2014
Thought: This one is a bit more complex but still... use a dictionary to keep track of the nodes and their depths
"""



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if not root:
            return []
        dic = {}
        self.preOrderAndCount(root, 0, dic)
        result = [0 for i in range(max(dic.keys())+1)]
        for i, v in dic.items():
            result[i] = v
        return result

    def preOrderAndCount(self, node, depth, dic):
        if not node:
            return
        if depth in dic:
            dic[depth].append(node.val)
        else:
            dic[depth] = [node.val]
        self.preOrderAndCount(node.left, depth+1, dic)
        self.preOrderAndCount(node.right, depth+1, dic)
