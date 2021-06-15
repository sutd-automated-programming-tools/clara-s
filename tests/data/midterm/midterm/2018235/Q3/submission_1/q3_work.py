# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    sq = s**2
    return sq

def vol_frustum(top_area, bottom_area, height):
    a1 = top_area
    a2 = bottom_area
    h = height
    vol = (h/3)*(a1 + a2 + math.sqrt(a1*a2))
    return vol

def get_volume(s1, s2, height):
    top = area_square(s1)
    bottom = area_square(s2)
    vol = vol_frustum(top, bottom, height)
    return round(vol, 3)

