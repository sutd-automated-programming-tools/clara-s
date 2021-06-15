# MID-TERM EXAM: QUESTION 3
from math import *

def area_square(s):
    return s*s

def vol_frustum(top_area, bottom_area, height):
    return height*(top_area + bottom_area + sqrt(top_area *bottom_area))/3

def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    vol = vol_frustum(top_area, bottom_area, height)
    return vol