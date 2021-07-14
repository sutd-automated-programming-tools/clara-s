# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s**2

def vol_frustum(top_area, bottom_area, height):
    return (height/3)*(top_area+bottom_area+math.sqrt(top_area*bottom_area))

def get_volume(s1, s2, height):
    top = area_square(s1)
    btm = area_square(s2)
    h = height
    return round(vol_frustum(top, btm, h),3)