# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s**2

def vol_frustum(top_area,bottom_area,height):
    v = height/3*(top_area + bottom_area + (top_area * bottom_area)**0.5)
    return v

def get_volume(s1,s2,height):
    A1 = area_square(s1)
    A2 = area_square(s2)
    return round(vol_frustum(A1,A2,height),3)

