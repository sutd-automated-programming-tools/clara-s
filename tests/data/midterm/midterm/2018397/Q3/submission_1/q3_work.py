# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s*s
    return area

def vol_frustum(top_area, bottom_area, height):
    A1 = top_area
    A2 = bottom_area
    H = height
    volume = (H/3)*(A1+A2+math.sqrt(A1*A2))
    return volume

def get_volume(s1, s2, height):
    area_square1 = s1*s1
    area_square2 = s2*s2
    vol_frustum = (height/3)*(area_square1+area_square2+math.sqrt(area_square1*area_square2))
    return round(vol_frustum,3)

