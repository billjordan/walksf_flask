#!/usr/bin/python3.4
"""
This can be used since the work to walk from one intersection to another cannot be negative.
This is bounded from above by e + n log n where e = number of edges(14k * 2) and n = number of nodes (9k),
which should be fast enough for the purposes of this program.
"""
from priority_queue import *
# from graph import SF_graph_dijkstra

def dijkstra_search(graph, start, end, toPrint=False):
    """
    initializes and runs dijkstra search on sf graph
    """
    nodes_visited = 0
    S = {} #dict of relaxed Dnodes CNN -> Dnode; weight from start -> start is 0
    Q = Priority_queue(graph.get_nodes(), start) # min priority queue of unrelaxed nodes 
    #look at every node in Q in order based on estimated shortest path
    while not Q.empty():
        if toPrint:
            nodes_visited += 1
            print(nodes_visited)
        #u is the node with the estimated shortest path as Dnode,
        u = Q.pop_dnode()
#         input("")
#         print(u.get_node().get_cnn() in S)
        if u.get_node().get_cnn() in S: continue
        S[u.get_node().get_cnn()] = u
        for v in graph.children_of(u.get_node()):
            Q.push_dnode(relax(u, Dnode(v), graph.get_edge(u.get_node(), v).get_work()))
            
    #build a list with the path backwards
    path = [S[end.get_cnn()].get_node()]
    prev_node = S[end.get_cnn()].get_pi()
    while prev_node is not None:
        path.append(prev_node.get_node())
        prev_node = S[path[-1].get_cnn()].get_pi()
    
    revpath = []
    for i in range(len(path)):
        revpath.append(path.pop(-1))
        
    return revpath
        
    



def relax(u, v, w):
    """
    relaxes the edge from u -> v
    w is the weight from u - >
    u and v are Dnodes connected by an edge
    returns v
    """
    if v.get_d() > u.get_d() + w:
        v.set_d(u.get_d() + w)
        v.set_pi(u)
        
    return v
         
    
#     print(q.pop())
#     n = q.pop()
#     print(n)
#     q.push(n.get_node(), 3)
#     while not q.empty():
#         print(q.pop(),  "\t", end="")