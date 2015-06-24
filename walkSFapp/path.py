from node import SF_intersection
class Path(object):
    """
    Path is a list of SF_intersection(node)s 
    """
    def __init__(self, node):
        self.node_list = [node]
        self.length = 0
        self.weight = 0
        
    def add_node(self, graph, new_node):
        last_node = self.node_list[-1]
        self.node_list.append(new_node)
        edge = graph.get_edge(last_node, new_node)
        self.length += edge.get_length()
        self.weight += edge.get_work()
        
    def get_weight(self):
        return self.weight
    
    def get_length(self):
        return self.length
    
    def get_node_list(self):
        return self.node_list
    
    def __str__(self):
        res = ""
        for node in self.node_list:
            res += "{} - > ".format(node.get_streets())
            
        return res[:-5]
        
    def __lt__(self, other):
        return self.get_weight() < other.get_weight()
    
    def add_path(self, graph, other):
        for node in other.get_node_list():
            self.add_node(graph, node)
            
    def PHPstring(self):
        """
        returns a string of nodes seperated by spaces that php can explode
        """
        res = ""
        for node in self.node_list:
            res += str(node) + " "
        return res[:-1]
    
    
def makePathFromDijk(graph, dijkList):
        """
        dijkList is list of SF_intersections
        """
        node = dijkList[0]
        path = Path(node)
        for node in dijkList[1:]:
            path.add_node(graph, node)
        
        return path
        
        