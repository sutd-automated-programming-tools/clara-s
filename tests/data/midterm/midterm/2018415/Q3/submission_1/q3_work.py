# MID-TERM EXAM: QUESTION 3

import math 

def area_square(s):
    area = s**2
    return (area)

def vol_frustum(top_area, bottom_area, height):
    t = top_area
    b = bottom_area
    h = height
    v = float((h/3)*(t+b+(t*b)**0.5))
    return (v)

def get_volume(s1, s2, height):
    a1 = s1**2
    a2 = s2**2
    h = height
    v = float((h/3)*(a1+a2+(a1*a2)**0.5))
    return (v)
