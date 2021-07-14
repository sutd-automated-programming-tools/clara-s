# MID-TERM EXAM: QUESTION 3

import math


def area_square(s):
    area = s**2
    return area

def vol_frustum(top_area, bottom_area, height):
    vol = (height/3) * (top_area + bottom_area + (top_area * bottom_area)**0.5)
    return vol

def get_volume(s1, s2, height):
    top = area_square(s1)
    bottom = area_square(s2)
    h = height
    volume = vol_frustum(top, bottom, h)
    return volume