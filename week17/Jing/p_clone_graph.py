"""
From: https://oj.leetcode.com/problems/clone-graph/
Author: Jing Zhou
Date: Jul 12, 2014
Thought: the traversal of graph. BFS. use of a queue.
"""



# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node
        mapNode = {}
        newGraph = UndirectedGraphNode(node.label)
        mapNode[node] = newGraph
        q = collections.deque()
        q.append(node)
        while q:
            nd = q.popleft()
            for nb in nd.neighbors:
                if nb not in mapNode:
                    newnb = UndirectedGraphNode(nb.label)
                    mapNode[nb] = newnb
                    mapNode[nd].neighbors.append(newnb)
                    q.append(nb)
                else:
                    mapNode[nd].neighbors.append(mapNode[nb])
        return newGraph
