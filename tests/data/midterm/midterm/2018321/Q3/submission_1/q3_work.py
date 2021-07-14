# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area_s = s * s
    return area_s


def vol_frustum(top_area, bottom_area, height):
    A1 = (top_area)
    A2 = (bottom_area)
    H = (height)
    volume = ((H/3) * (A1 + A2 + math.sqrt(A1*A2)))
    return volume

def get_volume(s1, s2, height):
    area1 = (area_square(s1))
    area2 = (area_square(s2))
    volume = (vol_frustum(area1 , area2, height))
    return round (volume,3)
