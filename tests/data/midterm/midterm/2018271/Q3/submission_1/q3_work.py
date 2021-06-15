# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area_of_square = s*s
    return area_of_square

def vol_frustum(top_area, bottom_area, height):
    A1 = top_area
    A2 = bottom_area
    H = height
    volume = (H/3)*(A1 + A2 + math.sqrt((A1)*(A2)))
    return volume

def get_volume(s1, s2, height):
    a1 = area_square(s1)
    a2 = area_square(s2)
    volume_ans = vol_frustum(a1, a2, height)
    return round(volume_ans,3)
