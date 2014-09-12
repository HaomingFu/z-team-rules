"""
From: https://oj.leetcode.com/problems/merge-k-sorted-lists/
Author: Jing Zhou
Date: Sep 10, 2014
Thought: use a priority queue. which is heapq in python
Tags: linked list, sort, merge
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        h = []
        res = None
        head = None
        for node in lists:
            if node:
                heapq.heappush(h, (node.val, node))
        while h:
            v, smallest = heapq.heappop(h)
            if not res:
                res = smallest
                head = res
            else:
                res.next = smallest
                res = res.next
            nextInList = smallest.next
            if nextInList:
                heapq.heappush(h, (nextInList.val, nextInList))
        return head
