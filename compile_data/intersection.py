#!/usr/bin/python3.4
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
    
    def hash(self):
        return self.CNN
    
    def getStreets(self):
        return self.streets
    
    def hasStreet(self, street):
        return street in self.streets
    
    def getLoc(self):
        return self.loc
    
    def getCNN(self):
        return self.CNN
    
    def getElev(self):
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
    
def loadIntersections(file="intersections.csv", toPrint = True):
    """
    returns a dict of intersections
    """
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