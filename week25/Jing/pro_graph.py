"""
breadth first search, connected components and mesure
the resilience of a network
"""
from collections import deque
def bfs_visited(ugraph, start_node):
    """ breath first search of a graph
    """
    queue = deque()
    visited = set([start_node])
    queue.append(start_node)
    while queue:
        node = queue.popleft()
        for neighbor in ugraph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

def cc_visited(ugraph):
    """compute the connected components of a graph
    """
    remaining_nodes = set(ugraph.keys())
    connected_comps = []
    while remaining_nodes:
        node = None
        for node in remaining_nodes:
            break
        component = bfs_visited(ugraph, node)
        connected_comps.append(component)
        remaining_nodes = remaining_nodes - component
    return connected_comps

def largest_cc_size(ugraph):
    """compute the largest connected component of a graph
    """
    components = cc_visited(ugraph)
    return max(map(len, components)) if components else 0

def compute_resilience(ugraph, attack_order):
    """ compute the resilience of a graph
    """
    size = []
    size.append(largest_cc_size(ugraph))
    for node in attack_order:
        for neighbor in ugraph[node]:
            ugraph[neighbor].remove(node)
        del ugraph[node]
        size.append(largest_cc_size(ugraph))
    return size
