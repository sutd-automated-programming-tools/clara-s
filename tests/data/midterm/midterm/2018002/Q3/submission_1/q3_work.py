# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s**2

def vol_frustum(t, b, h):
    return h / 3 * ( t + b + ( t * b )**0.5 )

def get_volume(s1, s2, h):
    t = area_square(s1)
    b = area_square(s2)
    return vol_frustum(t, b, h)