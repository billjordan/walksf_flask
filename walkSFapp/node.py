#!/usr/bin/python3.4
from intersection import Intersection
class Node(object):
    def __init__(self, uid):
        #unique id
        self.uid = uid
        
    def get_id(self):
        return self.uid
    
    def __str__(self):
        return self.uid
    
    def __repr__(self):
        return self.uid
    
    def __eq__(self, other):
        return self.uid == other.get_id()
    
    def __ne__(self, other):
        return not self == other
  
  
    
class SF_intersection(Node, Intersection):
    def __init__(self, cnn, streets, loc, elev):
        """
        cnn -> uid str
        streets -> list of streets
        loc -> Location(lat, long)
        elev -> int elevation (m)
        """
        self.CNN = cnn
        self.uid = cnn
        self.streets = streets  #list of strings
        self.loc = loc
        self.elev = elev
        
#     def get_cnn(self):
#         """
#         returns unique identifier
#         """
#         return self.uid
# 
#     def get_streets(self):
#         """
#         returns list of streets
#         order has no meaning
#         """
#         return self.streets
#     
#     def get_loc(self):
#         """
#         returns Location object(lat, long)
#         """
#         return self.loc
#     
#     def get_elev(self):
#         """
#         returns elevation integer meters
#         """
#         return self.elev
    
    
    def __hash__(self):
        """
        SF_intersections are unique by their uid
           
        """
        return int(self.uid)