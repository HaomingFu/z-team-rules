"""
From: https://oj.leetcode.com/problems/copy-list-with-random-pointer/
Author: Jing Zhou
Date: Jul 30, 2014
Thought: Iterate the linked list twice. I think once should also be doable. Will work on that.
Tags: linked-list, list, pointer
"""



class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return head
        nodeDict = {}
        newHead = RandomListNode(head.label)
        nodeDict[head] = newHead
        p = head.next
        q = newHead
        while p:
            nextNode = RandomListNode(p.label)
            q.next = nextNode
            nodeDict[p] = nextNode
            q = nextNode
            p = p.next

        p = head
        q = newHead
        while p:
            if p.random:
                q.random = nodeDict[p.random]
            p = p.next
            q = q.next
