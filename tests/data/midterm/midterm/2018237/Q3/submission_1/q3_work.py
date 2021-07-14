# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    sq_area = s * s
    return sq_area

def vol_frustum(a1, a2, h):
    frust_vol = (float(h)/3)(float(a1) + float(a2) + math.sqrt(float(a1)*float(a2)))
    return float(frust_vol)

def get_volume(s1, s2, height):
    s1 = area_square(s1)
    s2 = area_square(s2)
    vol = vol_frustrum(s1, s2, height)
    return round(vol, 3)