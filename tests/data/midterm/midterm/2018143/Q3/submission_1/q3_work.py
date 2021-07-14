# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    sq_area = s**2
    return sq_area

def vol_frustrum(top_area, bottom_area, height):
    vol = (height/3)*(top_area + bottom_area +math.sqrt(top_area*bottom_area))
    return vol

def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    vol =vol_frustrum(top_area, bottom_area, height)
    return round(vol,3)
