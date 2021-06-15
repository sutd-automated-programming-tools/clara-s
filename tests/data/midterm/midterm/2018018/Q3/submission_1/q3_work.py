# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    A = s**2
    return A

def vol_frustum(top_area, bottom_area, height):
    volume = (height/3)*(top_area + bottom_area + (top_area*bottom_area)**0.5)
    return volume

def get_volume(s1, s2, height):
    A1 = s1**2
    A2 = s2**2
    volume = (height/3)*(A1 + A2 + (A1*A2)**0.5)
    return volume

