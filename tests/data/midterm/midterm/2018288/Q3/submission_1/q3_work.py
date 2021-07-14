# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s**2

def vol_frustum(top_area, bottom_area, height):
    a1 = top_area
    a2 = bottom_area
    output = (height/3.0)*(a1+a2+((a1*a2)**0.5))
    return output
    

def get_volume(s1, s2, height):
    A1 = area_square(s1)
    A2 = area_square(s2)
    return round(vol_frustum(A1,A2,height),3)