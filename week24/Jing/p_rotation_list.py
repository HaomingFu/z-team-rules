"""
From: https://oj.leetcode.com/problems/rotate-list/
Author: Jing Zhou
Date: Sep 10, 2014
Thought: fast, slow pointer variation
Tags: linked list
"""



class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head or k==0:
            return head
        fast = slow = head
        while k > 0:
            if not fast.next:
                fast.next = head
            fast = fast.next
            k -= 1
        while fast.next and fast.next != head:
            fast = fast.next
            slow = slow.next
        if not fast.next:
            fast.next = head
        newHead = slow.next
        slow.next = None
        return newHead
