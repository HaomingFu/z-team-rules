""" Jing: 3/20/2014
This is a good one. Used recursion
http://oj.leetcode.com/problems/swap-nodes-in-pairs/
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(head):
    print("value of head", head.val)
    if not head or not head.next:
        return head
    new_head = head.next
    print("head", head.val)
    print("head next:", head.next.val)
    new_next = head.next.next
    print("next, next:", new_next.val)
    head.next.next = head
    print("next, next:", new_next.val)
    head.next = swapPairs(new_next)
    return new_head

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

new_head = swapPairs(a)
while(new_head):
    print("new list:", new_head.val)
    new_head = new_head.next

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        new_head = head.next
        new_next = head.next.next
        head.next.next = head
        head.next = self.swapPairs(new_next)
        return new_head
"""
