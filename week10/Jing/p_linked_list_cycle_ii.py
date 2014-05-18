"""
From: http://oj.leetcode.com/problems/linked-list-cycle-ii/
Author: Jing Zhou
Date: May 18, 2014
Thought: This one is basically the same as the last one, just need a third pointer. But be careful about the conditions... I was hesitate to add a flag but did it after all
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if not head:
            return None
        n1 = n2 = n3 = head
        hasTail = False
        while n1 and n1.next and n2:
            n1 = n1.next.next
            n2 = n2.next
            if n1 == n2:
                hasTail = True
                break
        if not hasTail:
            return None
        while n3 and n2 and n3 != n2:
            n3 = n3.next
            n2 = n2.next
        return n2
