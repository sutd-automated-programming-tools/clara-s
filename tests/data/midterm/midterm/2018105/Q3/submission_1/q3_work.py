# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s**2
    return area

def vol_frustum(top_area, bottom_area, height):
    A1 = top_area
    A2 = bottom_area
    H = height
    Volume = (H/3)(A1 + A2 + math.sqrt(A1*A2))
    return Volume

def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    vol = vol_frustum()
    return vol