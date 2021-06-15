# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return pow(s, 2)

def vol_frustum(t, b, h):
    v = (h/3) * (t + b + math.sqrt(t * b))
    return v

def get_volume(s1, s2, h):
    t = area_square(s1)
    b = area_square(s2)
    return round(vol_frustum(t, b, h), 3)
