# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area_square = s**2
    return area_square

def vol_frustum(top_area, bottom_area, height):
    
    A1 = top_area
    A2 = bottom_area
    H = height
    vol_frustum = H/3*(A1+A2+math.sqrt(A1*A2))
    return vol_frustum

def get_volume(s1, s2, height):

    get_volume = round(vol_frustum(area_square(s1), area_square(s2), height), 3)
    return get_volume