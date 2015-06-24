#!/usr/bin/python3.4
from intersection import loadIntersections

if __name__ == '__main__':
    dic = loadIntersections()
    fout = open("sorted_ints.csv", "w")
    for key in sorted(dic.keys()):
        fout.write(dic[key].getCSVLine())
    fout.close()