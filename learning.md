## Topic

### Graphs

Basics

- representation: 
- DFS: recursive, iterative(with stack)
- BFS: iterative(with queue)

#### Application

- s-t connectivity(BFS, DFS)
- cycle detection in undirected graphs(DFS, BFS)
- bipartite problem: BFS, coloring (the condition is no cycle with odd number of nodes)
- if a directed graph is strongly connected: BFS, then BFS in the reversed graph
- topological ordering: find a node with no incoming edges then delete it, recursicely compute.
