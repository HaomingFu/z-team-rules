# From: https://oj.leetcode.com/problems/binary-tree-postorder-traversal/
# Accepted.
# Recursive solution
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        res = []
        if root != None:
            res.extend(self.postorderTraversal(root.left))
            res.extend(self.postorderTraversal(root.right))
            res.append(root.val)
            return res
        else:
            return []



