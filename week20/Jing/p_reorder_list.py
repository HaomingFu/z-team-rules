"""
From: https://oj.leetcode.com/problems/reorder-list/
Author: Jing Zhou
Date: Aug 17, 2014
Thought: this one used two common operations: reverse a list and find the mid point of a list... And also merge two lists. It's a good practice on linked list
Tags: linked list, list
"""



class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if not head or not head.next:
            return head
        mid = self.findMid(head)
        mid = self.reverse(mid)
        start = head
        while mid and start:
            p = mid.next
            mid.next = start.next
            start.next = mid
            mid = p
            start = start.next.next
        start = mid
        return head
    def reverse(self, root):
        new_root = None
        while root:
            nextNode = root.next
            root.next = new_root
            new_root = root
            root = nextNode
        return new_root

    def findMid(self, head):
        p = head
        q = head.next
        while q:
            q = q.next
            if q:
                q = q.next
                p = p.next
        res = p.next
        p.next = None
        return res
