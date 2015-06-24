#!/usr/bin/python3.4
import math
def calc_work(delta_x, delta_y, mass=80, mu_k=.7):
    """
    returns the work done by a person walking up a grade with the components dx and dy
    walking downhill will be considered the same as walking on flat ground
    """
    #displacement along theta
    if delta_y < 0:
        delta_y = 0
    hyp = math.sqrt(delta_x**2 + delta_y**2)
    print("hyp = {}".format(hyp))
    theta = math.atan(float(delta_y)/delta_x)
    print("theta = {}".format(theta))
    grav = 9.81
    work = (mass * grav) * (math.sin(theta) + mu_k) * hyp
    return work

if __name__ == '__main__':
    done = False
    while not done:
        delta_x = input("dx: ")
        delta_y = input("dy: ")
        if str(delta_x).lower() == "quit" or str(delta_y).lower() == "quit":
            done = True
            break
        try:
            print(calc_work(float(delta_x), float(delta_y)))
        except(ValueError):
            print("dx and dy must be numbers")