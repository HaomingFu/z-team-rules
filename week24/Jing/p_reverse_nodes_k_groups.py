"""
From: https://oj.leetcode.com/problems/reverse-nodes-in-k-group/
Author: Jing Zhou
Date: Sep 10, 2014
Thought: Skill set: Reverse linked list and recursion
Tags: recursion, linked list, list
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        if length < k or k<=1:
            return head
        current = head
        prev = None
        nex = None
        count = 0
        while current and count < k:
            nex = current.next
            current.next = prev
            prev = current
            current = nex
            count += 1
        if nex:
            head.next = self.reverseKGroup(nex, k)
        return prev
