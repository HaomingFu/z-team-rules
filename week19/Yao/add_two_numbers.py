# From: https://oj.leetcode.com/problems/add-two-numbers/
# Status: Accepted
# Date:  August 4

class ListNode:
    def __init__(self, x):
        self.val =
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        res = ListNode(0)
        remain = 0
        head = res
        while l1 and l2:
            head.next = ListNode((l1.val + l2.val + remain) % 10)
            remain = (l1.val + l2.val + remain) // 10
            head = head.next
            l1 = l1.next
            l2 = l2.next
        while l2:
            head.next = ListNode((l2.val + remain) % 10)
            remain = (l2.val + remain) //10
            head = head.next
            l2 = l2.next
        while l1:
            head.next = ListNode((l1.val + remain) % 10)
            remain = (l1.val + remain) // 10
            head = head.next
            l1 = l1.next
        if remain:
            head.next = ListNode(remain)
        return res.next

