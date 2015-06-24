#!/usr/bin/python3.4
from intersection import *
from geopy.distance import great_circle
import math


#calculates the distance between to Locations - lat and long coords
#geopy might suit my needs
# def distance(loc1, loc2):
#     earth_radius = float(6373000) #approximate meters

#returns distance between two locations in meters
#this might not be accurate enough
def distance(loc1, loc2):
    return great_circle((loc1.getY(), loc1.getX()), (loc2.getY(), loc2.getX())).meters

def calc_work(delta_x, delta_y, mass=80, mu_k=.7):
    """
    returns the work done by a person walking up a grade with the components dx and dy
    walking downhill will be considered the same as walking on flat ground
    """
    #displacement along theta
    if delta_y < 0:
        delta_y = 0
    hyp = math.sqrt(delta_x**2 + delta_y**2)
#     print("hyp = {}".format(hyp))
    if delta_x == 0:
        pass
    theta = math.atan(float(delta_y)/delta_x)
#     print("theta = {}".format(theta))
    grav = 9.81
    work = (mass * grav) * (math.sin(theta) + mu_k) * hyp
    return work

if __name__ == '__main__':
    dic = loadIntersections()
    in1 = input("Enter CNN:")
    in2 = input("Enter CNN:")
    print(dic[in1])
    print(dic[in2])
    x = distance(dic[in1].get_loc(), dic[in2].get_loc())
    print(x)
    print(type(x))