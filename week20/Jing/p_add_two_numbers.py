"""
From: https://oj.leetcode.com/problems/add-two-numbers/
Author: Jing Zhou
Date: Aug 17, 2014
Thought: Easy but don't ignore the last node
Tags: Linked list, list, math
"""



class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        l3 = ListNode(0)
        p = l3
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            newNode = ListNode(carry%10)
            p.next = newNode
            p = p.next
            carry = carry/10
        if carry:
            newNode = ListNode(carry)
            p.next = newNode

        return l3.next
