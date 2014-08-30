#!/usr/bin/env python
# encoding: utf-8

# From: https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/
# Status: Accepted
# Date: August 30, 2014
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicate(self, head):
        if not head or not head.next:
            return head
        iter = head
        map = [head.val]
        while iter.next:
            if not iter.next.val in map:
                map.append(iter.next.val)
                iter = iter.next
            else:
                iter.next = iter.next.next

        return head
