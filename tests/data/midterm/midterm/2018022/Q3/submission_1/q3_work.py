# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    ans = s * s
    return ans

def vol_frustum(top_area, bottom_area, height):
    vol = (height/3) * (top_area + bottom_area + math.sqrt(top_area * bottom_area))
    return vol 

def get_volume(s1, s2, height):
    first = area_square(s1)
    second = area_square(s2)
    total_vol = round(vol_frustum(first, second, height), 3)
    return total_vol