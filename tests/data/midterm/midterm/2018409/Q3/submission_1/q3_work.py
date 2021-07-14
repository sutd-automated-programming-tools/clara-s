# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s*s

def vol_frustum(top_area, bottom_area, height):
    value = height/3*(top_area + bottom_area + math.sqrt(top_area*bottom_area))
    return value

def get_volume(s1, s2, height):
    
    top = area_square(s1)
    bottom = area_square(s2)
    result = vol_frustum(top, bottom, height)
    return round(result,3)
                     