# MID-TERM EXAM: QUESTION 3

import math 
def area_square(s):
    areaofsq = s*s
    return float(areaofsq)

def vol_frustum(top_area, bottom_area, height):
    vol = height/3 * (top_area + bottom_area + math.sqrt(top_area*bottom_area))
    return round(vol,3)

def get_volume(s1,s2,height):

    top_area = area_square(s1) #compute area of side1
    bottom_area = area_square(s2) #compute area of side2
    vol_frustum(top_area, bottom_area, height) #call vol_frustum to evaluate volume
    return get_volume