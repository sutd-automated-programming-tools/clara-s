# MID-TERM EXAM: QUESTION 3

import math
def area_square(s):
    return s*s

def vol_frustum(top_area, bottom_area, height):
    A1 = top_area
    A2 = bottom_area
    vol = (height/3)*(A1 + A2 + math.sqrt(A1 * A2))
    return vol

def get_volume(s1, s2, height):
    volume = vol_frustum(area_square(s1), area_square(s2), height)
    return round(volume, 3)
