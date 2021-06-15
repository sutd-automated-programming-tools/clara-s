# MID-TERM EXAM: QUESTION 3

from math import sqrt

def area_square(s):
    area=s*s
    return area
def vol_frustum(ta,ba,h):
    v=(h/3)*(ta+ba+sqrt(ta*ba))
    return v
def get_volume(s1,s2,h):
    a1=area_square(s1)
    a2=area_square(s2)
    v=vol_frustum(a1,a2,h)
    return round(v,3)
