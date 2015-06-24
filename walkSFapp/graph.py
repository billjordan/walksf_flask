#!/usr/bin/python3.4
from edge import SF_street
from node import SF_intersection
class Digraph(object):
    """
    directed graph
    """
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    
    def add_node(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    
    def add_edge(self, edge):
        src = edge.get_source()
        dest = edge.get_destination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    
    def children_of(self, node):
        for edge in self.edges[node]:
            yield edge.get_destination()
    
    def has_node(self, node):
        return node in self.nodes
    
    def __str__(self):
        res = ''
        for key in self.edges.keys():
            for dest in self.edges[key]:
                res = res + str(key) + '->' + str(dest) + '\n'
        return res[:-1]
    
class SF_graph(Digraph):
    """
    Directed graph of the SF street grid
    Nodes are SF_intersection
    Edges are SF_street
    all nodes are connected in both directions, but the paths are different 
    """
    def add_edge(self, edge):
        #add the street that was given
        src = edge.get_source()
        dest = edge.get_destination()
        
        #make sure the nodes are in the graph
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        
        #if the edge is not already in the graph add it
        if edge not in self.edges[src]:
            self.edges[src].append(edge)
            
        
        #add the reverse of the street if it is not already in the graph
        reverse_street = SF_street(dest, src, edge.get_streetname())
        if reverse_street not in self.edges[dest]:
            self.add_edge(reverse_street)
                          
        #if street and reverse of street are both in graph function will exit
        
        
    def __str__(self):
        res = ''
        for key in self.edges.keys():
            for edge in self.edges[key]:
                res = res + "{} -> {} || sn: {}; len: {}; elev_ch: {}\n".format(edge.get_source(), edge.get_destination(), edge.get_streetname(), edge.get_length(), edge.get_elev_change())
                
        return res[:-1]
    
    def get_edge(self, src, dest):
#         print type(self.edges)
#         print type(self.edges[])
        if src not in self.nodes:
            raise ValueError("Source node {} does not exist".format(src))
        if dest not in self.nodes:
            raise ValueError("Destination node {} does not exist".format(dest))
        for edge in self.edges[src]:
            if edge.get_destination() == dest:
                return edge
        raise ValueError("There is no edge from src:{} to dest:{}".format(src, dest))
    
    def get_edges(self):
        """
        returns the dict of edges
        """
        return self.edges
    
    def get_nodes(self):
        return self.nodes
    

            

if __name__ == '__main__':
    from intersection import loadIntersections
    from street import load_streets
    ints = loadIntersections()
    streets = load_streets()
    
    twenty1_folsom = "24079000"
    twenty2_folsom = "24077000"
    shotwell_21 = "24080000"
    shotwell_22 = "24078000"
    twenty1 = "1105000"
    twenty2 = "1187000"
    shotwell = "11839000"
    folsom = "5696000"
    intList = [twenty1_folsom, twenty2_folsom, shotwell_21, shotwell_22]
    streetList = [folsom, shotwell, twenty1, twenty2]
    graph = SF_graph()
    for node in intList:
        node = ints[node]
        sf_node = SF_intersection(node.get_cnn(), node.get_streets(), node.get_loc(), node.get_elev())
        graph.add_node(sf_node)
    
    for edge in streetList:
        edge = streets[edge]
        node = ints[edge.get_start()]
        start = SF_intersection(node.get_cnn(), node.get_streets(), node.get_loc(), node.get_elev())
        node = ints[edge.get_end()]
        end = SF_intersection(node.get_cnn(), node.get_streets(), node.get_loc(), node.get_elev())
        sf_edge = SF_street(start, end, edge.get_streetname())
        graph.add_edge(sf_edge)
        
    print(graph)
    print(graph.nodes)
