from graph import *
from node import *
from edge import *
def build_graph(i_dict, s_dict, toPrint=False):
    """
    takes an intersection dictionary and a street dictionary
    returns a SF_graph()
    """
    intersection_dict = i_dict
    street_dict = s_dict
    
    #create a dict of SF_intersections from intersection_dict
    sf_intersections = {}

    for key in intersection_dict.keys():
        intersection = intersection_dict[key]
        sf_intersections[key] = (SF_intersection(intersection.get_cnn(), intersection.get_streets(), intersection.get_loc(), intersection.get_elev()))
        
    if toPrint:
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
        
    if toPrint:
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
    return graph