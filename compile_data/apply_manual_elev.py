#!/usr/bin/python3.4
from intersection import *
man_ints = "manual_elev.csv"
api_ints = "intersections.csv"
manual_dict = loadIntersections(man_ints)
api_dict = loadIntersections(api_ints)


for key in manual_dict.keys():
    api_dict[key] = manual_dict[key]
    
fout = open("fixed_intersections.csv", "w")
for key in sorted(api_dict.keys()):
    fout.write(api_dict[key].getCSVLine())
    
fout.close()