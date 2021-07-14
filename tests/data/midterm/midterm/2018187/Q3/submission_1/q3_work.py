# MID-TERM EXAM: QUESTION 3

import math


def area_square(s):
    return s**2

def vol_frustum(top_area, bottom_area, h):
    return (h/3)*(top_area + bottom_area + math.sqrt(top_area*bottom_area))

def get_volume(s1,s2,h):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    output = vol_frustum(top_area,bottom_area,h)
    return round(output,3)

