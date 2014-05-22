# non-recursive version
# From: https://oj.leetcode.com/problems/binary-tree-postorder-traversal/
#
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        res = []
        stack = []
        p = root
        while p!= None:
            if p.left != None:
                old = p
                p = p.left
                old.left = None
                stack.append(old)
            elif p.right!=None:
                old = p
                p = p.right
                old.right = None
                stack.append(old)
            else:
                res.append(p.val)
                if len(stack) > 0:
                    p = stack.pop()
                else:
                    break
            return res
