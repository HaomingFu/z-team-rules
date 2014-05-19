"""
From: http://oj.leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
Author: Jing Zhou
Date: May 19, 2014
Thought: This one is not very hard. I think I now get the hang of linked lists now.
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy
        repeat = False
        while node and node.next and node.next.next:
            if node.next.val == node.next.next.val:
                repeat = True
                node.next = node.next.next
            elif repeat:
                node.next = node.next.next
                repeat = False
            else:
                node = node.next
        if repeat:
            node.next = node.next.next
        return dummy.next
