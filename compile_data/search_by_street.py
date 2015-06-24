#!/usr/bin/python3.4
from intersection import *

dic = loadIntersections("fixed_intersections.csv")
done = False
while not done:
    street1 = input("Enter street name:")
    street2 = input("Enter street name:")
    if str(street1).lower() == "quit" or str(street2).lower() == "quit":
        done = True
        break
    else:
        hasStreet = False
        for key in dic.keys():
            if dic[key].hasStreet(street1.upper()) and dic[key].hasStreet(street2.upper()):
                print(dic[key])
                hasStreet = True
        if not hasStreet:
            print("record does not exist")