# MID-TERM EXAM: QUESTION 3

import math as ma

def area_square(s):
    square_a = s**2
    return square_a

def vol_frustum(top_area, bottom_area, height):
    fru_vol = height/3*(top_area + bottom_area + ma.sqrt(top_area * bottom_area))
    return fru_vol

def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    volume = vol_frustum(top_area, bottom_area, height)
    return round(volume,3)