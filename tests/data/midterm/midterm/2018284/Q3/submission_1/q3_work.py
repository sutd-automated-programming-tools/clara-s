# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s*s

def vol_frustum(top_area, bottom_area, height):
    return (h/3)*(a+b+(a*b)**0.5)

def get_volume(s1, s2, height):
    a1 = area_square(s1)
    a2 = area_square(s2)
    return round( vol_frustrum(a1,a2,height),3 )