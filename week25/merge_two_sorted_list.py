#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/merge-two-sorted-lists/
# Date: Sep. 14
# Status: AC

class Solution:
    # @param two ListNodes
    # @return a listNode
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        p = head
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                p = p.next
                l1 = l1.next
            else:
                p.next = l2
                p = p.next
                l2 = l2.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return head.next
