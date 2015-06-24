#!/usr/bin/python3.4
from geopy.distance import great_circle

class Location(object):
    """
    has x and y floats for long and lat
    """
    
    def __init__(self, x, y):
        try:
            x = float(x)
            y = float(y)
        except(ValueError):
            raise ValueError("X and Y must either be floats, or parseable to floats")
        self.x = x
        self.y = y
 
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getLat(self):
        return self.y
    
    def getLong(self):
        return self.x
    
    def getLongStr(self):
        return str(self.x)
    
    def getLatStr(self):
        return str(self.y)
    
    def __eq__(self, loc2):
        return self.getX() == loc2.getX() and self.getY() == loc2.getY()
    
    def get_distance(self, other):
        """
        returns the absolute value of the distance between self and other in meters
        implemented by geopy.distance.great_circle 
        """
        return great_circle((self.getY(), self.getX()), (other.getY(), other.getX())).meters
    