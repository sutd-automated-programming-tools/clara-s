# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s**2

def vol_frustum(top_area, bottom_area, height):
    res = height * (top_area + bottom_area + (top_area*bottom_area)**(1/2))/3
    return round(res,3)

def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    return vol_frustum(top_area, bottom_area, height)