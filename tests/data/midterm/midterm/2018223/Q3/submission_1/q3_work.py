# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = float(s**2)
    return area

def vol_frustum(top_area, bottom_area, height):
    vol = float((height/3)*(top_area + bottom_area + math.sqrt(top_area * bottom_area)))
    return vol

def get_volume(s1, s2, height):
    top_area = float(area_square(s1))
    bottom_area = float(area_square(s2))
    out = vol_frustum(top_area, bottom_area, height)
    out = round(out, 3)
    return out
