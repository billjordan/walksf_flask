#!/usr/bin/python3.4
from getIntersections import getIntersectionDict
from intersection import Location, Intersection


def makeDictWithLoc(file = "cnn_loc_elev.csv", streetDict = getIntersectionDict()):
    """
    streetDict maps cnn to list of streets
    """
    intersectionFile = open(file, mode='r')
    #dic is dict: cnn -> intersection{cnn, streetList, cnn, elev(None for now)} 
    dic = {}
    for line in intersectionFile:
        line = line.split(',')
        cnn = line[0]
        if cnn not in dic.keys():
            dic[cnn] = Intersection(cnn, streetDict[cnn], Location(line[1], line[2]))
        else:
            #this intersection is alread in dic, long and lat should match
            if not dic[cnn].getLoc() == Location(line[1], line[2]):
                assert False
    return dic

# Location and Intersection are in intersection.py

# class Location(object):
#     """
#     has x and y floats for long and lat
#     """
#     
#     def __init__(self, x, y):
#         try:
#             x = float(x)
#             y = float(y)
#         except(ValueError):
#             raise ValueError("X and Y must either be floats, or parseable to floats")
#         self.x = x
#         self.y = y
#  
#     def getX(self):
#         return self.x
#     
#     def getY(self):
#         return self.y
#     
#     def getLat(self):
#         return self.y
#     
#     def getLong(self):
#         return self.x
#     
#     def getLongStr(self):
#         return str(self.x)
#     
#     def getLatStr(self):
#         return str(self.y)
#     
#     def __eq__(self, loc2):
#         return self.getX() == loc2.getX() and self.getY() == loc2.getY()
# 
# class Intersection(object):
#     """
#     Intersection is:
#     a list of two streets, order is not important
#     CNN this is unique and the hash value, comes from datasf
#     location -> comrpised of two floats
#     elevation -> I dont have this yet, set it to None
#     """
#     def __init__(self, CNN, streets, loc, elev = None):
#         self.CNN = CNN
#         self.streets = streets
#         self.loc = loc
#         self.elev = elev
#     
#     def hash(self):
#         return self.CNN
#     
#     def getStreets(self):
#         return self.streets
#     
#     def hasStreet(self, street):
#         return str in street
#     
#     def getLoc(self):
#         return self.loc
#     
#     def getCNN(self):
#         return self.CNN
#     
#     def getElev(self):
#         return self.elev
#     
#     def setElev(self, elev):
#         self.elev = elev
#     
#     def __eq__(self, int2):
#         return self.getCNN() == int2.getCNN()
#     
#     def __str__(self):
#         return "CNN:\t{}\nSTR1:\t{}\nSTR2:\t{}\nLAT:\t{}\nLONG:\t{}\nELEV:\t{}".format(self.CNN, self.streets[0], self.streets[1], self.loc.getLat(), self.loc.getLong(), self.elev)
#     
#     def getCSVLine(self):
#         """
#         returns the Intersection in a csv line
#         cnn,street,street,lat,long,elev
#         used to store intersection in csv file
#         """
#         return "{},{},{},{},{},{}".format(self.CNN, self.streets[0], self.streets[1], self.loc.getLat(), self.loc.getLong(), self.elev)
    
if __name__ == '__main__':
    dic = makeDictWithLoc()
    
    done = False
    while not done:
        user_in = input("Enter CNN:")
        if str(user_in).lower() == "quit":
            done = True
            break
        else:
            try:
                print(dic[user_in].getCSVLine())
            except(KeyError):
                print("record does not exist")