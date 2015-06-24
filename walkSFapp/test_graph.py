"""
test street grid bounded by 
N Sacramento St
W Baker St
S Sutter St
E Steiner St
Should have 53 edges and 33 nodes
O ~ 3 ** 12 + 2 ** 16 paths ~ 600k

26630000 steiner and wilmot is not in inttersections
26642000 pine and scott are not in intersections
nodes: 31
edges: 47
"""
from intersection import loadIntersections
from street import load_streets
from build_graph import build_graph
from graph import Digraph
from dynamic_search import *
import random
from node import SF_intersection
import sys
import json
from sys import stderr
from dijkstra_search import dijkstra_search
from path import makePathFromDijk


def main(start = None, end = None):
    #list of strings containing every street with an
    #intersection in the grid 
    exp_node_num = 31
    exp_edge_num = 47
    streets_in_grid = ["SACRAMENTO ST", "BAKER ST", "SUTTER ST", "STEINER ST", "PERINE PL", "WILMOT ST", "BRODERICK ST", "DIVISADERO ST", "SCOTT ST", "PIERCE ST", "CALIFORNIA ST", "PINE ST", "BUSH ST"]
    int_dic = loadIntersections(toPrint=False)
    ints_in_grid = {}
    #if both streets for intersection are in grid, add the intersection to ints_in_grid
    for key in int_dic.keys():
        if int_dic[key].get_streets()[0] in streets_in_grid and int_dic[key].get_streets()[1] in streets_in_grid:
            ints_in_grid[key] = int_dic[key]
    
    # for key in ints_in_grid.keys():
    #     print(ints_in_grid[key].get_streets())
        
    # print(len(ints_in_grid))
    
    #get every street where start int and end int are in test Grid
    all_streets = load_streets(toPrint=False)
    streets_in_grid = {}
    for key in all_streets.keys():
        if all_streets[key].get_start() in ints_in_grid.keys() and all_streets[key].get_end() in ints_in_grid.keys():
            streets_in_grid[key] = all_streets[key]
    
#     for key in streets_in_grid.keys():
#         sne = streets_in_grid[key].get_start_name_end()
#         print("{}->{}->{}".format(ints_in_grid[sne[0]].get_streets(), sne[1], ints_in_grid[sne[2]].get_streets()))
#     print(len(streets_in_grid))
    digraph = build_graph(ints_in_grid, streets_in_grid)
#     print("Args: {}".format(sys.argv))
#     print("Arg length: {}".format(len(sys.argv)))
    if len(sys.argv) == 3:
        if sys.argv[1] in ints_in_grid.keys() and sys.argv[2] in ints_in_grid.keys():
            start = sys.argv[1]
            end = sys.argv[2]
        else:
            print("invalid start or end node")
            assert False
    else:
        start = random.choice(list(ints_in_grid.keys()))
        end = random.choice(list(ints_in_grid.keys()))
        while end == start:
            end = random.choice(list(ints_in_grid.keys()))
    start_int = ints_in_grid[start]
    end_int = ints_in_grid[end]
    start_node= SF_intersection(start_int.get_cnn(), start_int.get_streets(), start_int.get_loc(), start_int.get_elev())
    end_node= SF_intersection(end_int.get_cnn(), end_int.get_streets(), end_int.get_loc(), end_int.get_elev())
    bf_path = search(digraph, start_node, end_node)
    print("start:{} - {}".format(start_int.get_streets(), start_int.get_cnn()))
    print("end:{} - {}".format(end_int.get_streets(), end_int.get_cnn()))
    print("brute force: " + str(bf_path))
    print(bf_path.get_weight())
    print()
    dp_path = dsearch(digraph, start_node, end_node)
    print()
    print("dynamic p:   " + str(dp_path))
    print(dp_path.get_node_list())
    print(dp_path.get_weight())
    print("\nDystra:")
    dpath = dijkstra_search(digraph, start_node, end_node, toPrint=False)
    dyspath = makePathFromDijk(digraph, dpath)
    print(dyspath)
    print(dpath)
    print(dyspath.get_weight())
            

if __name__ == '__main__':
    main()