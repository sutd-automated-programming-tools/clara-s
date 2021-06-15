# MID-TERM EXAM: QUESTION 3

import math

#square the length of square to find the area
def area_square(s):
    area = s**2
    return area

def vol_frustum(top_area, bottom_area, height):
    part1 = height/3
    total_area = top_area + bottom_area 
    sr = math.sqrt(top_area + bottom_area)
    vol = part1 * (total_area + sr)
    return vol

def get_volume(s1, s2, height):
    top_area = def area_square(s1):
    bottom_area = def area_square(s2):
    #find the area of top_area (A1) by putting new variable s1 into the area func
    #find the area of bottom_area (A2) by putting new variable s2 into the area func
    
    finalvol = def vol_frustum(top_area, bottom_area, height)
    return round (float(finalvol,3))

    #after finding the top n bottom areas put the new areas into the formula in the volume function
    #round off the final vol of the frustum to 3dp
