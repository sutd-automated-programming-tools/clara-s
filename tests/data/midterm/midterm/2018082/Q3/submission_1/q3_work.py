# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return round(float(s**2),3)

def vol_frustum(top_area, bottom_area, height):
    t = top_area
    b = bottom_area
    h = height
    square = math.sqrt(b*t)
    vol = (h/3)*(t+b+square)
    return round(vol,3)
    

def get_volume(s1, s2, height):
    area1 = area_square(s1)
    area2 = area_square(s2)
    return vol_frustum(area1,area2,height)
