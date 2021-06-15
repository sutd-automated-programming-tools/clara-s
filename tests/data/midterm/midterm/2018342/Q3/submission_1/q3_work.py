# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s**2

def vol_frustum(top_area, bottom_area, height):
    return height / 3.0 * (top_area + bottom_area + (top_area * bottom_area) ** 0.5)

def get_volume(s1, s2, height):
    top_a = area_square(s1)
    bot_a = area_square(s2)
    return round(vol_frustum(top_a, bot_a, height), 3)
