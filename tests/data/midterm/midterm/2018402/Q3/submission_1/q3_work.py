# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s**2

def vol_frustum(top_area, bottom_area, height):
    return (height / 3) * (top_area + bottom_area + ((top_area * bottom_area) ** 0.5))
    

def get_volume(s1, s2, height):
    a1 = area_square(s1)
    a2 = area_square(s2)
    volume = vol_frustum(a1, a2, height)
    volume = round(volume, 3)
    return volume