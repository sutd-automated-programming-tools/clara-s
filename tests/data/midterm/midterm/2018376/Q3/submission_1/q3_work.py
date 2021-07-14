# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s**2

def vol_frustum(top_area, bottom_area, height):
    A1 = top_area
    A2 = bottom_area
    H = height
    return (H/3)*(A1+A2+math.sqrt(A1*A2))

def get_volume(s1,s2,height):
    top_a = area_square(s1)
    bottom_a = area_square(s2)
    output = vol_frustum(top_a, bottom_a, height)
    return round(output,3)