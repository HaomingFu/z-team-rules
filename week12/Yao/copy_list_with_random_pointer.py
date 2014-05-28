# From: https://oj.leetcode.com/problems/copy-list-with-random-pointer/
# Date: May 28, 2014
# Status: Accepted

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RodomListNode
    def copyRandomList(self, head):
        if not head:
            return None
        phead = head
        # inerst nodes the original list
        while phead:
            tmp = RandomListNode(phead.label)
            tmp.next = phead.next
            phead.next = tmp
            phead = phead.next.next

        phead = head
        chead = head.next
        while phead:
            if phead.random:
                chead.random = phead.random.next
            phead = phead.next.next
            if phead.next.next:
                chead = chead.next

        phead = head
        chead = head.next
        pchead = chead
        while phead and phead.next.next:
            phead.next = phead.next.next
            pchead.next = pchead.next.next
            phead = phead.next
            pchead = pchead.next
        phead.next = None

        return chead
