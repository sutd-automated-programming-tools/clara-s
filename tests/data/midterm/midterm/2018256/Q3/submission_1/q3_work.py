# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    ans = s**2
    return ans

def vol_frustum(top_area, bottom_area, height):
    ans = height / 3 * (top_area + bottom_area + math.sqrt(top_area * bottom_area))
    return ans

def get_volume(s1, s2, height):
    top = area_square(s1)
    bottom = area_square(s2)
    vol = round(vol_frustum(top,bottom,height),3)
    return vol
