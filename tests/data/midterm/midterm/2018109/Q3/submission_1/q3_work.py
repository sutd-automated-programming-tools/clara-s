# MID-TERM EXAM: QUESTION 3
from math import sqrt

def area_square(s):
    return s ** 2

def vol_frustum(t, b, h):
    return round(h * (t + b + sqrt(t * b) ) / 3,3)
def get_volume(s1,s2,h):
    t = area_square(s1)
    b = area_square(s2)
    return vol_frustum(t,b,h)