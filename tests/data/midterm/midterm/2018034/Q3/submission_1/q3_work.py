# MID-TERM EXAM: QUESTION 3

import math
def area_square(s):
    return s**2
def vol_frustum(top_area,bottom_area, height):
    Volume = height/3*(top_area + bottom_area + math.sqrt(top_area*bottom_area))
    return Volume
def get_volume(s1,s2,height):
    a1 = area_square(s1)
    a2 = area_square(s2)
    vol = vol_frustum(a1,a2,height)
    return round(vol,3)