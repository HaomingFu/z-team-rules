"""
From: http://oj.leetcode.com/problems/merge-two-sorted-lists/
Author: Jing Zhou
Date: May 10, 2014
Though: I need to solve more list related problem... This
one is not very hard
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param two ListNodes
    # @return a ListNode

    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        head, sub = [l1, l2] if l1.val < l2.val else [l2, l1]
        while head and sub:
            if not head.next:
                head.next = sub
                break
            while head.val < sub.val and head.next and head.next.val < sub.val:
                head = head.next
            node = sub.next
            sub.next = head.next
            head.next = sub
            sub = node
            head = head.next

        return l1 if l1.val < l2.val else l2
