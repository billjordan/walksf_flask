#!/usr/bin/python3.4
"""
when the api cannot return an elevation it returns -32768
find these interstections and manually fix them manually
"""
from intersection import loadIntersections
from get_elev_from_openmaps import *

def retry_bad_elevs(dic, outFile):
    key = "key goes here"
#     print(len(dic))
#     assert False
    vals = dic.keys()
    for val in vals:
        loc = dic[val].getLoc()
        dic[val].setElev(getElev(key, loc.getLat(), loc.getLong()))
        outFile.write("{}\n".format(dic[val].getCSVLine()))

if __name__ == '__main__':
    dic = loadIntersections()

    fout = open("bad_elev.csv", "w")
    bad_elev_dict = {}
    for key in sorted(dic.keys()):
        if int(dic[key].getElev()) == -32768:
            bad_elev_dict[key] = dic[key]
            fout.write("{}\n".format(dic[key].getCSVLine()))
    fout.close()
    print(len(bad_elev_dict))
    new_elevs = open("retry_bad_elevs", "w")
    retry_bad_elevs(bad_elev_dict, new_elevs)
    new_elevs.close()
    