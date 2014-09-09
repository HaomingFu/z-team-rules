"""
From: https://oj.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
Author: Jing Zhou
Date: Aug 19, 2014
Thought: This is O(nlgn), this is another O(n) solution out there
Tags: linked list, recursion
"""



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if not head:
            return head
        if not head.next:
            return TreeNode(head.val)
        head, root, nextNode = self.findRoot(head)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(nextNode)
        return root
    def findRoot(self, head):
        slow = q = head
        fast = head.next
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                q = slow
                slow = slow.next
        nextNode = slow.next
        root = TreeNode(slow.val)
        q.next = None
        if q == slow:
            head = None
        return head, root, nextNode
