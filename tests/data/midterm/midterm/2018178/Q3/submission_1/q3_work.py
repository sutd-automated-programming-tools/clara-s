# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s**2

def vol_frustum(t, b, h):
    return h/3*(t+b+math.sqrt(t*b))

def get_volume(s1, s2, h):
    t = area_square(s1)
    b = area_square(s2)
    v = vol_frustum(t, b, h)
    return round(v, 3)
