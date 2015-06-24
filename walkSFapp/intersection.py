#!/usr/bin/python3.4
from location import Location
from os.path import os
class Intersection(object):
    """
    Intersection is:
    a list of two streets, order is not important
    CNN this is unique and the hash value, comes from datasf
    location -> comrpised of two floats
    elevation -> int(meters) repr by string
    """
    def __init__(self, CNN, streets, loc, elev = None):
        self.CNN = CNN
        self.streets = streets
        self.loc = loc
        if elev is not None:
            try:
                self.elev = int(elev)
            except(ValueError):
                raise ValueError("Elevation must be integer - meters above sea level; use 'None' if elevation is unknown")
        else:
            self.elev = None
    
    def __hash__(self):
        return int(self.CNN)
    
    def get_streets(self):
        return self.streets
    
    def has_street(self, street):
        return street in self.streets
    
    def get_loc(self):
        return self.loc
    
    def get_cnn(self):
        return self.CNN
    
    def get_elev(self):
        return self.elev
    
    def setElev(self, elev):
        self.elev = elev
    
    def __eq__(self, int2):
        return self.getCNN() == int2.getCNN()
    
    def __str__(self):
        return "CNN:\t{}\nSTR1:\t{}\nSTR2:\t{}\nLAT:\t{}\nLONG:\t{}\nELEV:\t{}".format(self.CNN, self.streets[0], self.streets[1], self.loc.getLat(), self.loc.getLong(), self.elev)
    
    def getCSVLine(self):
        """
        returns the Intersection in a csv line
        cnn,street,street,lat,long,elev
        used to store intersections in csv file
        """
        return "{},{},{},{},{},{}".format(self.CNN, self.streets[0], self.streets[1], self.loc.getLat(), self.loc.getLong(), self.elev)
    
    def get_distance(self, other):
        """
        returns the distance between this intersection and other intersection in meters
        """
        return self.loc.get_distance(other.get_loc())
    
def loadIntersections(file="intersections.csv", toPrint = True):
    """
    returns a dict of intersections
    """
    file = os.path.dirname(__file__) + "/" + file
    inFile = open(file, mode='r')
    dic = {}
#     lineNumber = 0
    for line in inFile:
        line = line.split(',')
        dic[line[0]] = Intersection(line[0], [line[1], line[2]], Location(line[4], line[3]), line[5])
    inFile.close()
    if toPrint:
        print("# of intersections = {}".format(len(dic)))
    return dic
    
if __name__ == '__main__':
    dic = loadIntersections()

    done = False
    while not done:
        user_in = input("Enter CNN:")
        if str(user_in).lower() == "quit":
            done = True
            break
        else:
            try:
                print(dic[user_in])
            except(KeyError):
                print("record does not exist")