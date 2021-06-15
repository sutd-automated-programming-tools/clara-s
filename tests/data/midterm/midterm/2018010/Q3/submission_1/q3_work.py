# MID-TERM EXAM: QUESTION 3

from math import sqrt

def area_square(s):
    return s * s

def vol_frustum(top_area, bottom_area, height):
    
    rooted = sqrt(top_area * bottom_area)
    brac = top_area + bottom_area + rooted
    vol = height * brac / 3
    return vol

def get_volume(s1, s2, height):
    
    ta = area_square(s1)
    ba = area_square(s2)
    ans = vol_frustum(ta, ba, height)
    rounded = round(ans, 3)
    return rounded
