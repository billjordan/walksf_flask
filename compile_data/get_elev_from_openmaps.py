#!/usr/bin/python3.4
from getIntersectionsWithLoc import makeDictWithLoc
import requests
global key
key = "get key here: http://developer.mapquest.com/web/products/open"


def getElev(key, lat, long, unit = 'm'):
    """
    streets is a list of two strings of streets
    """
    req_str = "http://open.mapquestapi.com/elevation/v1/profile?key={}&latLngCollection={},{}&unit={}".format(key, lat, long, unit)
    r = requests.get(req_str)
    rj = r.json()
    return rj["elevationProfile"][0]["height"]

if __name__ == '__main__':
    if key == "get key here: http://developer.mapquest.com/web/products/open":
        print(key)
        raise ValueError("invalid api key")
#     fout = open("intersection.csv",'w')
    dic = makeDictWithLoc()
    vals = dic.keys()
    for val in vals:
        loc = dic[val].getLoc()
        dic[val].setElev(getElev(key, loc.getLat(), loc.getLong()))
#         fout.write("{}\n".format(dic[val].getCSVLine()))
         
#     fout.close()
    