# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return float(s**2)
print (area_square(2))

def vol_frustum(top_area, bottom_area, height):
    a1 = top_area
    a2 = bottom_area
    h = height
    return ((h/3) * (a1 + a2 + (math.sqrt(a1*a2))))
def get_volume(s1, s2, height):
    return (round((vol_frustum(area_square(s1),area_square(s2),height)), 3))