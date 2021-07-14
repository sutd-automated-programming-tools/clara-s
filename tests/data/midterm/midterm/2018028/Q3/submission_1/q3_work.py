# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):

    area = s*s
    return area


def vol_frustum(top_area, bottom_area, height):
    
    a1 = (top_area) 
    a2 = (bottom_area)
    diff = a1 + a2 + math.sqrt(a1 * a2 )
    vol = (height) / 3 * (diff)
    return vol

def get_volume(s1, s2, height):
    
    a_t = area_square(s1)
    a_b = area_square(s2)
    vol = vol_frustum(a_t,a_b,height)
    return vol
