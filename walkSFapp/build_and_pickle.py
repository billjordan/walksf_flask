#!/usr/bin/python3.4
"""
Pickling is the process of creating a binary representation of an object that can be stored outside of the program
This will prevent me from having to build the graph from the data every time the program will run, since the data will not change,
and decrease the load time.
"""
from intersection import loadIntersections
from street import load_streets
from node import SF_intersection
from edge import SF_street
from graph import SF_graph
import pickle


def main():
    intersection_dict = loadIntersections()
    street_dict = load_streets()
    
    #create a dict of SF_intersections from intersection_dict
    sf_intersections = {}

    for key in intersection_dict.keys():
        intersection = intersection_dict[key]
        sf_intersections[key] = (SF_intersection(intersection.get_cnn(), intersection.get_streets(), intersection.get_loc(), intersection.get_elev()))
        
    print(len(sf_intersections))
    #create a list of streets from street_dict   
    sf_streets = []
    for key in street_dict.keys():
        street = street_dict[key]
        if street.get_start() == street.get_end():
            #Ramsel Ct loops around on itself with no intersections and should be excluded from the graph
            #exclude this case and any like it
            continue
        sf_streets.append(SF_street(sf_intersections[street.get_start()], sf_intersections[street.get_end()], street.get_streetname()))
        
    print(len(sf_streets))

    graph = SF_graph()
    
    for key in sf_intersections.keys():
        graph.add_node(sf_intersections[key])
        
#     print(len(graph.nodes))
    
    for edge in sf_streets:
#         print(type(edge))
#         print(type(edge.get_source()))
#         print(edge.get_source() in graph.nodes)
#         print(graph.nodes)
        graph.add_edge(edge)
#         except(ValueError):
#             pass
        
    sf_graph_out = open("sf_graph.pickle", "wb")
    pickle.dump(graph, sf_graph_out)
        

if __name__ == '__main__':main()    