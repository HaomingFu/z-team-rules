"""

The problem is how to choose next node to consider.
Here is the node with the smallest distance to the original node and
Not considered yet.
"""
import heapq
def dijkstra(graph, source, target = None):
    queue = [(0, source, [])]
    seen = set()
    while True:
        cost, v, path = heapq.heappop(queue)
        if v not in seen:
            path = path + [v]
            seen.add(v)
            if v == target:
                return cost, path
            for nextNode, c in graph[v].items():
                if nextNode not in seen:
                    heapq.heappush(queue, (cost + c, nextNode, path))
                print(queue)



if __name__=='__main__':
    # A simple edge-labeled graph using a dict of dicts
    graph = {'a': {'b':14, 'c':9, 'd':7},
             'b': {'a':14, 'c':2, 'e':9},
             'c': {'a':9, 'b':2, 'd':10, 'f':11},
             'd': {'a':7, 'c':10, 'f':15},
             'e': {'b':9, 'f':6},
             'f': {'c':11, 'd':15, 'e':6}}

    #dist, path = dijkstra(graph, source='a')
    #print(dist)
    #print(path)
    print(dijkstra(graph, 'a', 'e'))
