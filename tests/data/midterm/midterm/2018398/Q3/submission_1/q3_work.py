# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return round(float(s ** 2), 3)

def vol_frustum(top_area, bottom_area, height):
    ans = ((height)/3) * (top_area + bottom_area + math.sqrt(top_area * bottom_area))
    return ans

def get_volume(s1, s2, height):
    ans = (height/3) * (area_square(s1) + area_square(s2) + math.sqrt(area_square(s1) * area_square(s2)))
    return round(ans, 3)
