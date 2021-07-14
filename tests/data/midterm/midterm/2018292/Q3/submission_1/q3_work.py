# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    a = s ** 2
    return round (a,3)

def vol_frustum(top_area, bottom_area, height):
    ta = top_area
    ba = bottom_area
    h = height
    v = (h/3) * (ta + ba + math.sqrt(ta*ba))
    return round (v,3)

def get_volume(s1,s2,height):
    aOne = area_square(s1)
    aTwo = area_square(s2)
    h = height
    vol = vol_frustum(aOne, aTwo, h)
    return round (vol,3)
