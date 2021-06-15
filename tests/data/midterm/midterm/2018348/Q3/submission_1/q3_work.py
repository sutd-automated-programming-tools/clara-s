# MID-TERM EXAM: QUESTION 3

import math 

def area_square(s):
    a = s**2
    return a

def vol_frustum(top_area, bottom_area, height):
    v = (height/3) * (top_area + bottom_area + math.sqrt((top_area*bottom_area)))
    return v

def get_volume(s1, s2, height):
    b = area_square(s1)
    c = area_square(s2)
    d = vol_frustum(b,c,height)
    return d

