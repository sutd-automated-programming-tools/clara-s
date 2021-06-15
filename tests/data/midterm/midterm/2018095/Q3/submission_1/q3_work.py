# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s**2
    return area

def vol_frustum(top_area,bottom_area, height):
    vol = height*(top_area+bottom_area+(top_area*bottom_area)**0.5)/3
    print(vol)
    return vol


def get_volume(s1,s2,h):
    a1 = area_square(s1)
    a2 = area_square(s2)
    vol = vol_frustum(a1,a2,h)
    return vol