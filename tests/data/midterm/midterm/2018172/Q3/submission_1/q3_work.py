# MID-TERM EXAM: QUESTION 3

from math import sqrt

def area_square(s):
    area = s * s
    return round(area,3)

def vol_frustum(top_area, bottom_area, height):
    vol = (height/3)*(top_area + bottom_area + sqrt(top_area * bottom_area))
    return round(vol,3)

def get_volume(s1, s2, height):
    t1 = area_square(s1)
    t2 = area_square(s2)
    ans = vol_frustum(t1, t2, height)
    return round(ans,3)
