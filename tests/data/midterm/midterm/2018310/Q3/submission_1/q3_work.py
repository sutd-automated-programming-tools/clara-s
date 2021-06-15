# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s*s
    return area

def vol_frustrum(top_area, bottom_area, height):
    volume = (height / 3) * \
    (top_area + bottom_area + (top_area * bottom_area)**0.5)
    return volume

def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    volume = vol_frustrum(top_area, bottom_area, height)
    return volume

