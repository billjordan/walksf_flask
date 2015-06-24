from dijkstra_search import dijkstra_search
import random
import pickle
import sys
from path import makePathFromDijk
from os.path import os

def main():
    graph_file = os.path.dirname(__file__) + "/sf_graph.pickle"
    gragh_pickle_in = open(graph_file, "rb")
    graph = pickle.load(gragh_pickle_in)
    cnns = graph.get_nodes()
    if len(sys.argv) == 3:
        if sys.argv[1] in cnns and sys.argv[2] in cnns:
            start = sys.argv[1]
            end = sys.argv[2]
        else:
            print("invalid start or end node")
            assert False
    else:
        start = random.choice(list(cnns))
        end = random.choice(list(cnns))
        while end == start:
            end = random.choice(list(cnns))
    cnnList = list(cnns)
    start_ind = cnnList.index(start)
    end_ind = cnnList.index(end)
    start_node = cnnList[start_ind]
    end_node = cnnList[end_ind]
    path = dijkstra_search(graph, start_node, end_node)
    path = makePathFromDijk(graph, path)
    print(path.PHPstring())
    
if __name__ == '__main__':
    main()