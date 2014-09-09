# From: https://oj.leetcode.com/problems/linked-list-cycle-ii/
# Accepted
# Date: May 22, 2014
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if (not head) or (not head.next):
            return None
        fast = head
        slow = head
        fast = fast.next.next
        slow = slow.next
        while fast!= slow:
            if (not fast) or (not fast.next):
                return None
            fast = fast.next.next
            slow = slow.next
        slow = head
        while  fast != slow:
            fast = fast.next
            slow = slow.next
        return slow
