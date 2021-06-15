# MID-TERM EXAM: QUESTION 3

import math as m
def area_square(s):
    area = s**2
    return area

def vol_frustum(top_area, bottom_area, height):
    a1 = top_area
    a2 = bottom_area
    h = height
    
    volume = h/3*(a1 + a2 + (m.sqrt(a1*a2)))
    return volume

def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    result = vol_frustum(top_area, bottom_area, height)
    return round(result, 3)