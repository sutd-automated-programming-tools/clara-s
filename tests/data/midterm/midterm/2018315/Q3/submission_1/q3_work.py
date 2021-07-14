# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s*s

def vol_frustum(top_area, bottom_area, height):
    vol = (height/3)*(top_area + bottom_area + (math.sqrt(top_area*bottom_area)))
    return vol

def get_volume(s1, s2, height):
    upper_area = area_square(s1)
    lower_area = area_square(s2)
    volume = vol_frustum(upper_area, lower_area, height)
    return volume
