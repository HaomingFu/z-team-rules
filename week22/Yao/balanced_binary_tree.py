#!/usr/bin/env python
# encoding: utf-8

class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        hl = self.getHeight(root.left)
        h2 = self.getHeight(root.right)
        if hl-hr<=1 and hl-hr>= -1:
            if self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            else:
                return False
        else:
            return False

    def getHeight(self, root):
        if not root:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
