#!/usr/bin/python3.4
#This file gets a dict[CNN] = [str1, str2]
#where str1 and str2 are the streets that make up the intersection
#Each intersection is listed twice but only the first entry is added to the dictionary

def getIntersectionDict(file = "List_of_Intersections_only.csv"):
    intersectionFile = open(file, mode='r')
    dic = {}
#     numLinesSkipped = 0
    for line in intersectionFile:
        line = line.split(',')
        if line[0] not in dic.keys():
            #skip first line
            if line[0] == "CNN": continue
            dic[line[0]] = [line[1], line[2]]
#         else:
#             numLinesSkipped += 1
#             print(numLinesSkipped)
    return dic

class intersection(object):
    """
    An intersection is a set of two streets(strings)
    """

if __name__ == '__main__':
    dic = getIntersectionDict()

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
        
