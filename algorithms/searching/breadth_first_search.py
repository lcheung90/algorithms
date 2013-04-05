"""
    breadth_first_search.py

    Iterative implementation of BFS algorithm on a graph.

    Breadth First Seach Overview:
    ------------------------
    Used when the search is limited to:
        -visit and inspecta node of a graph
        -gain access to visit the nodes that neighbor the 
         currently visited node

    Time Complexity: O(E + V)
        E = number of edges
        V = number of vertices (nodes)

    Pseudocode: https://en.wikipedia.org/wiki/Breadth-first_search
"""
from Queue import Queue

def bfs(graph,root,target):
    q = Queue()
    checked = []
    q.put(root)
    path = 0
    while not q.empty():
        v = q.get()
        if v == target:
           return checked
        elif v not in checked:
            for edge in graph[v]:
                if v not in checked:
                    q.put(edge)
            checked.append(v)
    return "Node "+str(target)+" is not in the graph."
