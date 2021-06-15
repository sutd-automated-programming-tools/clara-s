# MID-TERM EXAM: QUESTION 3

from math import sqrt

def area_square(s):
    return s**2

def vol_frustum(top_area, bottom_area, height):
    return (top_area + bottom_area + sqrt(top_area*bottom_area))*height/3

def get_volume(s1, s2, height):
    A1 = area_square(s1)
    A2 = area_square(s2)
    return round(float(vol_frustum(A1, A2, height)), 3)
