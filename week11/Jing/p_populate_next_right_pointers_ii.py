"""
From: https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
Author: Jing Zhou
Date: May 23, 2014
Thought: This is easy... but the recursive order is very important, first do this right child then the left...
"""



class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                node = root.next
                while node and not node.left and not node.right:
                    node = node.next
                if node:
                    root.left.next = node.left if node.left else node.right
        if root.right:
            node = root.next
            while node and not node.left and not node.right:
                node = node.next
            if node:
                root.right.next = node.left if node.left else node.right
            #root.right.next = self.findNext(root)
        self.connect(root.right)
        self.connect(root.left)

# rewritten...
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        if root.left:
           root.left.next = root.right if root.right else self.findNext(root)
        if root.right:
            root.right.next = self.findNext(root)
        self.connect(root.left)
        self.connect(root.right)


    def findNext(self, node):
        node = node.next
        while node and not node.left and not node.right:
            node = node.next
        if node and (node.left or node.right):
            return node.left if node.left else node.right
        return None
