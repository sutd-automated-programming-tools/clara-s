# MID-TERM EXAM: QUESTION 3

import math


def area_square(s):
    return s**2


def vol_frustum(top_area, bottom_area, height):
    volume = (float(height/3)) * float(top_area + bottom_area + math.sqrt(top_area * bottom_area))
    return volume


def get_volume(s1, s2, height):
    toparea = area_square(s1)
    btmarea = area_square(s2)
    output = vol_frustum(toparea, btmarea, height)
    return round(output, 3)
