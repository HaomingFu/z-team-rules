import heapq
def shortest_path(G, start, end):
   def flatten(L):       # Flatten linked list of form [0,[1,[2,[]]]]
      while len(L) > 0:
         yield L[0]
         L = L[1]

   q = [(0, start, ())]  # Heap of (cost, path_head, path_rest).
   visited = set()       # Visited vertices.
   while True:
      (cost, v1, path) = heapq.heappop(q)
      if v1 not in visited:
         visited.add(v1)
         if v1 == end:
            return list(flatten(path))[::-1] + [v1], cost
         path = (v1, path)
         for (v2, cost2) in G[v1].items():
            if v2 not in visited:
               heapq.heappush(q, (cost + cost2, v2, path))

def test():
    G = {'s':{'u':10, 'x':5},
            'u':{'v':1, 'x':2},
            'v':{'y':4},
            'x':{'u':3, 'v':9, 'y':2},
            'y':{'s':7, 'v':6}
            }
    print(shortest_path(G, 's', 'y'))
    print(shortest_path(G, 's', 'v'))

test()
