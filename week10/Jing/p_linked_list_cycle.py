"""
From: http://oj.leetcode.com/problems/linked-list-cycle/
Author: Jing Zhou
Date: May 18, 2014
Thought: This one is quite easy... just two pointers and advanve one by two and the other by one
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head:
            return False
        r1 = r2 = head
        while r1 and r1.next and r2:
            r1 = r1.next.next
            r2 = r2.next
            if r1 == r2:
                return True
        return False
