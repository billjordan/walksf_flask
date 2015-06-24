#!/usr/bin/python3.4
class Street(object):
    """
    cnn: unique id from datasf
    streetname: string
    start: intersection cnn
    end: intersection cnn
    """
    def __init__(self, cnn, streetname, start, end):
        self.cnn = cnn
        self.streetname = streetname
        self.start = start
        self.end = end
    
    
    def get_cnn(self):
        return self.cnn
    
    def get_streetname(self):
        return self.streetname
    
    def get_start(self):
        return self.start
    
    def get_end(self):
        return self.end
    
    def __eq__(self, street2):
        return self.get_cnn() == street2.get_cnn()
    
    def getCSVLine(self):
        return "{},{},{},{}".format(self.cnn, self.streetname, self.start, self.end)
    

def load_streets(inFile = "streets.csv", toPrint = True):
    """
    returns a dict cnn -> street(cnn, streetname, start intersection, end intersection)
    """
    streetFile = open(inFile, "r")
    streets = {} #dict of streets
    for line in streetFile:
        line = line.split(",")
        cnn = line[0]
        streetname = line[1]
        start = line[2]
        end = line[3][:-1]
        street = Street(cnn, streetname, start, end)
        streets[cnn] = street
    streetFile.close()
    if toPrint:
        print("# streets = {}".format(len(streets)))
    return streets

if __name__ == '__main__':
    load_streets()