# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s*s
    return area

def vol_frustum(top_area,bottom_area,height):
    ta = float(top_area)
    ba = float(bottom_area)
    h = float(height)
    vol = (h/3)*(ta+ba+(ta*ba)**0.5)
    return vol

def get_volume(s1,s2,height):
    a1 = area_square(s1)
    a2 = area_square(s2)
    h = float(height)
    volume = vol_frustum(a1,a2,h)
    return volume
