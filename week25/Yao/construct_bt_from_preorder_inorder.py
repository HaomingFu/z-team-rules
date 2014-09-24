#From: https://oj.leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Status:
# Date: Sep. 16

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        print(preorder[0])
        print(inorder)
        ix = inorder.index(preorder[0])
        left = self.buildTree(preorder[0:ix], inorder[0:ix])
        right = self.buildTree(preorder[ix+1:], inorder[ix+1:])
        root.left = left
        root.right = right

        return root


if __name__ == "__main__":
    preorder = [1,2]
    inorder = [2, 1]
    s = Solution()
    root = s.buildTree(preorder, inorder)
