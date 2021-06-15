# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s**2
    pass

def vol_frustum(top_area, bottom_area, height):
    return (height/3)*(top_area + bottom_area + math.sqrt(top_area * bottom_area))
    pass

def get_volume(s1, s2, height):
    h = height
    top = area_square(s1)
    bottom = area_square(s2)
    return round(vol_frustum(top, bottom, h),3)
    pass