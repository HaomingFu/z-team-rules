"""
From: https://oj.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Author: Jing Zhou
Date: Aug 27, 2014
Thought: About same with the one with the level traversal, there is alternative solutions using stacks/queues
Tags: BST, tree
"""



class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        dic = {}
        dic_indicator = {}
        self.preOrderAndCount(root, 0, dic, dic_indicator, True)
        result = [0 for i in range(max(dic.keys())+1)]
        for i, v in dic.items():
            result[i] = v if dic_indicator[i] else v[::-1]
        return result

    def preOrderAndCount(self, node, depth, dic, dic_indicator, indicator):
        if not node:
            return
        if depth in dic:
            dic[depth].append(node.val)
        else:
            dic[depth] = [node.val]
            dic_indicator[depth] = indicator
        self.preOrderAndCount(node.left, depth+1, dic, dic_indicator, not indicator)
        self.preOrderAndCount(node.right, depth+1, dic, dic_indicator, not indicator)
