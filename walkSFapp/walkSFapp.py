#!/usr/bin/python3.4
import pickle
from intersection import loadIntersections
from node import SF_intersection
from dynamic_search import *
import sys
from edge import SF_street
from dijkstra_search import dijkstra_search
from path import *

def main():
    sys.setrecursionlimit(100000)
#     print(sys.getrecursionlimit())
    gragh_pickle_in = open("sf_graph.pickle", "rb")
    graph = pickle.load(gragh_pickle_in)
    print(len(graph.nodes))
    twenty1_folsom = "24079000"
    twenty2_folsom = "24077000"
    int_list = loadIntersections()
    int1 = int_list[twenty1_folsom]
    int2 = int_list[twenty2_folsom]
    node1 = SF_intersection(int1.get_cnn(), int1.get_streets(), int1.get_loc(), int1.get_elev())
    node2 = SF_intersection(int2.get_cnn(), int2.get_streets(), int2.get_loc(), int2.get_elev())
    edge = graph.get_edge(node1, node2)
    print(edge.get_streetname())
    print(edge.get_length())
    print(edge.get_work())
    print(edge.get_source().get_streets())
    print(edge.get_destination().get_streets())
    for n in graph.children_of(node1):
        print(n)
    shortest_path = search(graph, node1, node2, toPrint=True)
    print(shortest_path)
    shortest_path = makePathFromDijk(graph, shortest_path)
    print(shortest_path)
#     for node_str in shortest_path.get_node_list():
#         print("{}  \n===\n||\n\\/\n".format(int_list[str(node_str)].get_streets()))
#            
    print(shortest_path.get_weight())
    print(shortest_path.get_length())
    print("------correct answer-------")
    ans = SF_street(node1, node2, "folsom")
#     print(ans.get_elev_change())
    print(ans.get_work())
    print(ans.get_length())
    
    print("Arrived")
    

    
if __name__ == '__main__':main()
