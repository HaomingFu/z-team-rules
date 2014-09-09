# From: https://oj.leetcode.com/problems/insertion-sort-list/
# Date: May 28, 2014
# Status: Accepted

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        pivot =  ListNode(-100000)
        pivot.next = head
        prev = head
        head = head.next
        while head:
            if head.val < prev.val:
                prev.next = head.next
                p = pivot
                pos = pivot.next
                while pos.val < head.val:
                    p = pos
                    pos = pos.next
                p.next = head
                head.next = pos
                head = prev.next
            else:
                prev = head
                head = head.next

        return pivot.next

