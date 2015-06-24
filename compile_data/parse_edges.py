#!/usr/bin/python3.4
"""
gets all valid edges(street segments from List_of_Streets_and_Intersections.csv)
valid edges have both nodes in intersection dict (some intersection might be missing)
"""
from intersection import loadIntersections
from street import Street

# int_dict = loadIntersections("fixed_intersections.csv")
# street_segments = open("street_segments.csv", 'r')
# # edges = open("streets.csv", "w")
# nodes = int_dict.keys()
# print('2796100sf0' in nodes)
# firstline = street_segments.readline()
# secondline = street_segments.readline()

# # print(firstline)
# fline = firstline.split(',')
# # print(fline)
# # print(len(fline))
# 
# # print(secondline)
# sline = secondline.split(',')
# # print(sline)
# # print(len(sline))
# #for line in street_segments:
# 
# # print(int_dict[sline[-1][:-1]])
# # print(int_dict[sline[-2]])
# 
# cnn = sline[0]
# streetname = sline[1]
# start = sline[-2]
# end = sline[-1][:-1]
# street1 = Street(cnn, streetname, start, end)
# 
# 
# print(street1.getCVSLine())
# 
# street_segments.close()

def makeStreetsCSV(intersection_file = "fixed_intersections.csv", street_segments_file = "street_segments.csv", streets_file = "new_streets.csv"):
    int_dict = loadIntersections(intersection_file)
    street_segments = open(street_segments_file, "r")
    streets = open(streets_file, "w")
    nodes = int_dict.keys()
    dic = {} #dict of cnn -> street
    repeatedStreets = 0
    streetMissingEnds = 0

    for line in street_segments:
        line = line.split(",")
        #skip first line
        if line[0] == "CNN": continue
        cnn = line[0]
        streetname = line[1]
        start = line[-2]
        end = line[-1][:-1]
        #dont repeat streets
        if cnn in dic.keys():
            repeatedStreets += 1
            continue
        #make sure both ends exist (a few or missing)
        if start in nodes and end in nodes:
            street = Street(cnn, streetname, start, end)
            dic[cnn] = street
        else:
            streetMissingEnds += 1
            
        
    print("# of repeated streets: {}\n# of streets missing ends: {}".format(repeatedStreets, streetMissingEnds))
    
    street_segments.close()
    
    for key in sorted(dic.keys()):
        streets.write("{}\n".format(dic[key].getCSVLine()))
        
    streets.close()
    
if __name__ == '__main__':
    makeStreetsCSV()