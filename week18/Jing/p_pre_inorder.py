"""
From: https://oj.leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Author: Jing Zhou
Date: Jul 15, 2014
Thought: Similar to the postorder and inorder one
Tags: tree, postorder, inorder
"""



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        startIn, startPre = 0, 0
        inEnd = preEnd = len(inorder)-1
        dic = {}
        for i, val in enumerate(inorder):
            dic[val] = i
        return self.buildBinaryTree(inorder, preorder, startIn, inEnd, startPre, preEnd, dic)

    def buildBinaryTree(self, inorder, preorder, inStart, inEnd, preStart, preEnd, dic):
        if inStart > inEnd or preStart > preEnd:
            return None
        rootVal = preorder[preStart]
        root = TreeNode(rootVal)
        k = dic[rootVal]
        root.left = self.buildBinaryTree(inorder, preorder, inStart, k-1, preStart+1, preStart+k-inStart, dic)
        root.right = self.buildBinaryTree(inorder, preorder, k+1, inEnd, preEnd-inEnd+k+1, preEnd, dic)
        return root
