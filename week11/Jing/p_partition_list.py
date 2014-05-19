"""
From: http://oj.leetcode.com/problems/partition-list/
Author: Jing Zhou
Date: May 19, 2014
Thought: Not very hard, but need to be careful... draw things out on a piece of paper helps. used a dummy head.
"""



# Deftion for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        dummy = ListNode(x-1)
        dummy.next = head
        node = dummy
        while node.next and node.next.val < x:
            node = node.next
        runner = node
        while runner and runner.next:
            if runner.next.val < x:
                tmp = runner.next
                runner.next = runner.next.next
                tmp1 = node.next
                node.next = tmp
                node.next.next = tmp1
                node = node.next
            else:
                runner = runner.next
        return dummy.next
