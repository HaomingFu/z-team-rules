"""
From: http://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/
Author: Jing Zhou
Date: May, 15, 2014
Thought: easy... but have to consider the case when removing the first node
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        first, second, i = head, head, 0
        while i < n:
            second = second.next
            i += 1
        if not second:
            return head.next
        while second.next:
            second = second.next
            first = first.next
        first.next = first.next.next
        return head
