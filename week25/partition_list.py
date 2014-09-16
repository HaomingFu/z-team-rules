#!/usr/bin/env python
# encoding: utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if not head or not head.next:
            return head
        lessHead = ListNode(0)
        greatHead = ListNode(0)
        lessCur = lessHead
        greatCur = greatHead
        cur = head
        while cur:
            if cur.val < x:
                lessCur.next = cur
                lessCur = lessCur.next
            else:
                greatCur.next = cur
                greatCur = greatCur.next
            cur = cur.next
            greatCur.next = None
            lessCur.next = greatHead.next
        return lessHead.next

