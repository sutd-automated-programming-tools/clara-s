# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s**2

def vol_frustum(top_area, bottom_area, height):
    volume = (top_area + bottom_area + math.sqrt(top_area*bottom_area))*height/3
    return volume

def get_volume(s1, s2, height):
    return vol_frustum(area_square(s1), area_square(s2), height)
