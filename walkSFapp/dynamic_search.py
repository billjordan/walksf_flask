#!/usr/bin/python3.4
"""
This is a weighed depth first search of a directed graph that utilizes dynamic programming to avoid recalculation.
A simple brute force with my dataset (approximately 9000 nodes with an average of 3 edges leaving each node) will not finish in a reasonable time frame. 
Dynammic programming for a graph of the street grid of San Francisco will probably use too much memory for my 1GB
Amazon server, and will probably take too long, but it will allow me to compare the results of searching with Dijkstra's algorithm.
"""
from node import SF_intersection
from edge import SF_street
from path import Path
from graph import Digraph
global num_calls

def dynamic_search(digraph, start, end, toPrint = False, visited = None, memo = None):
    """
    dynamic programming search of a weighted graph
    visited is a list of strings representing the nodes that have been visited in this path of the recursion tree
    visited is used to prevent looping
    memo is a dictionary of calculated shortest paths; node->path
    memo is used to prevent recalculation
    """
    if toPrint:
        print("start: {}; end: {};".format(start.get_streets(), end.get_streets()))
    if memo == None:
        memo = {}
    if visited == None:
        visited = [str(start)]
#         print(type(visited))
    else:
        visited += [str(start)]
#         print(str(start))
    path = Path(start)
    if start == end:
        return path
    shortest = None
    for node in digraph.children_of(start):
        if str(node) not in visited: #avoid cycles
            try:
                new_path = memo[(node, end)] #see if a best shortest path has been calculated from this node
            except(KeyError):
                new_path = dynamic_search(digraph, node, end, toPrint, visited, memo)#find the shortest for this child
            if new_path == None: #no valid path was found
                continue #try the next child
            if shortest == None or new_path < shortest:
                memo[(node, end)] = new_path
                shortest = new_path
    if shortest != None:#a shortest path was found
        path.add_path(digraph, shortest)
    else:#no children of this node found a valid path
        path = None
    # pop up
    return path
    
    
def bf_search(digraph, start, end, toPrint = False, visited = None):
    """
    search of a weighted graph
    number of paths is bounded by approximately 3 ** 9000
    this will not finish on the full graph
    this is for testing on small graphs
    visited is a list of strings representing the nodes that have been visited in this path of the recursion tree
    visited is used to prevent looping
    """
    global num_calls
    num_calls += 1
    if toPrint:
        if num_calls % 100000 == 0:print(num_calls)
    if toPrint:
        print("start: {}; end: {};".format(start.get_streets(), end.get_streets()))
    if visited == None:
        visited = [str(start)]
#         print(type(visited))
    else:
        visited = visited + [str(start)]
#         print(str(start))
    path = Path(start)
    if start == end:
        return path
    shortest = None
    for node in digraph.children_of(start):
        if str(node) not in visited: #avoid cycles
            new_path = bf_search(digraph, node, end, toPrint, visited)#find the shortest for this child
            if new_path == None: #no valid path was found
                continue #try the next child
            if shortest == None or new_path < shortest:
                shortest = new_path
    if shortest != None:#a shortest path was found
        path.add_path(digraph, shortest)
    else:#no children of this node found a valid path
        path = None
    # pop up
    return path

def search(digraph, start, end, toPrint=False):
    global num_calls    
    num_calls = 0
    path = bf_search(digraph, start, end, toPrint)
    print("bf calls: {}".format(num_calls))
    return path

def dsearch(digraph, start, end, toPrint=False):
    global num_calls    
    num_calls = 0
    path = dp_search(digraph, start, end, toPrint)
    print("dp calls: {}".format(num_calls))
    return path

def dp_search(digraph, start, end, toPrint = False, visited = None, memo = None):
    """
    search of a weighted graph
    number of paths is bounded by approximately 3 ** 9000
    this will not finish on the full graph
    this is for testing on small graphs
    visited is a list of strings representing the nodes that have been visited in this path of the recursion tree
    visited is used to prevent looping
    """
    global num_calls
    num_calls += 1
    if toPrint:
        if num_calls % 100000 == 0:print(num_calls)
#     if toPrint:
#         print("start: {}; end: {};".format(start.get_streets(), end.get_streets()))
    if visited == None:
        visited = [str(start)]
#         print(type(visited))
    else:
        visited = visited + [str(start)]
#         print(str(start))
    if memo == None:
        memo = {} #new dict
    path = Path(start)
    if start == end:
        return path
    shortest = None
    for node in digraph.children_of(start):
        if str(node) not in visited: #avoid cycles
            try:
                new_path = memo[(node, end)]
            except(KeyError):
                new_path = dp_search(digraph, node, end, toPrint, visited, memo)#find the shortest for this child
            if new_path == None: #no valid path was found
                continue #try the next child
            if shortest == None or new_path < shortest:
                memo[(node, end)] = new_path
                shortest = new_path
    if shortest != None:#a shortest path was found
        path.add_path(digraph, shortest)
    else:#no children of this node found a valid path
        path = None
    # pop up
    return path