# MID-TERM EXAM: QUESTION 3

import math


def area_square(s):
    return float(s*s)


def vol_frustum(top_area, bottom_area, height):
    return float(height*(top_area+bottom_area+math.sqrt(top_area*bottom_area))/3.0)


def get_volume(s1, s2, height):
    ta = area_square(s1)
    ba = area_square(s2)
    return round(vol_frustum(ta,ba,height),3)
