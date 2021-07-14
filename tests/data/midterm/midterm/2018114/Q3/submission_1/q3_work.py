# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    a = s**2
    return a
    pass

def vol_frustum(top_area, bottom_area, height):
    t = top_area
    b = bottom_area
    h = height
    volume = h/3*(t+b+math.sqrt(t*b))
    return volume
    pass

def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    V = vol_frustum(top_area, bottom_area, height)
    V = round(V,3)
    return V