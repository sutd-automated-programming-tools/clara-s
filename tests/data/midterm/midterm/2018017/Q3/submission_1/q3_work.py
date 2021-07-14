# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return (s ** 2)
    pass

def vol_frustum(top_area, bottom_area, height):
    return ((height/3) * (top_area + bottom_area + math.sqrt(top_area * bottom_area)))
    pass

def get_volume(s1, s2, height):
    out = vol_frustum(area_square(s1), area_square(s2), height)
    return round(out, 3)
    pass
