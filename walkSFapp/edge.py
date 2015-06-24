#!/usr/bin/python3.4
from utils import calc_work
from intersection import loadIntersections

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    
    def get_source(self):
        return self.src
    
    def get_destination(self):
        return self.dest
    
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)
    
    
    
class SF_street(Edge):
    def __init__(self, src, dest, streetname):
        """
        length, elev_change and work are computed at object initialization
        to get the value of work use get_work, not compute_work
        src and dest are type Intersection
        """
        self.src = src
        self.dest = dest
        self.streetname = streetname
        self.length = src.get_distance(dest)
        #elevation change is the change from src to dest
        #if dest is higher than src elev_change is > 0; if dest is lower than src elev_change is < 0
        self.elev_change = dest.get_elev() - src.get_elev()
        self.work = self.compute_work()
    
    def get_length(self):
        return self.length
    
    def get_elev_change(self):
        """
        returns an integer
        elevation change is the change from src to dest
        if dest is higher than src elev_change is > 0; if dest is lower than src elev_change is < 0
        """
        return self.elev_change
    
    def compute_work(self):
        """
        THIS SHOULD NOT BE CALLED OUTSIDE OF THE OF THE CLASS - USE GET_WORK
        returns the work done by a person walking up a grade with the components dx and dy
        walking downhill will be considered the same as walking on flat ground
        """
        return calc_work(self.length, self.elev_change)
    
    def get_work(self):
        """
        returns the work done by a person walking up a grade with the components dx and dy
        walking downhill will be considered the same as walking on flat ground
        """
        return self.work
    
    def get_streetname(self):
        return self.streetname
    
    def print_attributes(self):
        print("SRC:\n{}".format(self.src))
        print("DEST:\n{}".format(self.dest))
        print("STREET NAME: {}".format(self.streetname))
        print("STREET LENGTH: {}".format(self.length))
        print("ELEVATION CHANGE: {}".format(self.elev_change))
        print("WORK: {}".format(self.work))
        
    def __eq__(self, other):
        return self.src == other.get_source() and self.dest == other.get_destination()
    
        
if __name__ == '__main__':
    dic = loadIntersections()

    done = False
    while not done:
        int1 = input("Enter CNN:")
        int2 = input("Enter CNN:")
        if str(int1).lower() == "quit" or str(int2).lower() == "quit":
            done = True
            break
        else:
            street = SF_street(dic[int1], dic[int2], "test")
            street.print_attributes()