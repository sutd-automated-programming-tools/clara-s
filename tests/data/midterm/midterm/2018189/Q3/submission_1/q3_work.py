# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return float(s**2)

def vol_frustum(top_area, bottom_area, height):
    sq =  math.sqrt(top_area * bottom_area)
    vol = (height / 3)*(top_area + bottom_area + sq)
    return float(vol)

def get_volume(s1, s2, height):
    return round(vol_frustum(area_square(s1), area_square(s2), height), 3)