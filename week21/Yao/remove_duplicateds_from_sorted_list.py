#!/usr/bin/env python
# encoding: utf-8

#From: https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
#Status: wrong answers, why?
#Date: August 31
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicate(self, head):
        if not head or not head.next:
            return head
        map = [head.val]
        dup = []
        iter = head
        while iter.next:
            if  not iter.next.val in map:
                map.append(iter.next.val)
                iter = iter.next
            else:
                dup.append(iter.next.val)
                iter.next = iter.next.next
        pseudo_head = ListNode(0)
        pseudo_head.next = head
        iter =pseudo_head
        while iter.next:
            if not iter.next.val in dup:
                iter = iter.next
            else:
                iter.next = iter.next.next

        return pseudo_head.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(1)
    s = Solution()
    print(s.deleteDuplicate(head))
