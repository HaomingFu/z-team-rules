# From: https://oj.leetcode.com/problems/binary-tree-preorder-traversal/
# Accepted

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integer
    def preorderTraversal(self, root):
        res = []
        stack = []
        p = root
        if root:
            res.append(root.val)
        while p:
            #res.append(p.val)
            if p.left:
                res.append(p.left.val)
                parent = p
                p = p.left
                parent.left = None
                stack.append(parent)
            elif p.right:
                res.append(p.right.val)
                parent = p
                p = p.right
                parent.right= None
                stack.append(parent)
            else:
                if len(stack) > 0:
                    p = stack.pop()
                else:
                    break
        return res
if __name__ == "__main__":
    root = TreeNode(1)
    s = Solution()
    print(s.preorderTraversal(root))
