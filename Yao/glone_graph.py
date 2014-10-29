#!/usr/bin/env python
# encoding: utf-8

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def cloneGraph(self, node):
        if not node:
            return node

        root = UndirectedGraphNode(node.label)
        last, cp_last = [node], [root]
        hashmap = {}
        while last:
            current, cp_current = [], []
            n, i = len(last), 0
            while i < n:
                cur, cp_cur = last[i], cp_last[i]
                if cur.label in hashmap:
                    i += 1
                    continue
                hashmap[cur.label] = cur
                current += cur.neighbors
                cp_cur.neighbors = list(cur.neighbors)
                cp_current += cp_cur.neighbors
                i += 1
            last, cp_last = current, cp_current

        return root


