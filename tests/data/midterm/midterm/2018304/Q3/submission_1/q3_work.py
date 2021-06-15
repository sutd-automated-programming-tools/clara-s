# MID-TERM EXAM: QUESTION 3

import math
def area_square(s):
    area = s**2
    return area
def vol_frustum(top_area, bottom_area, h):
    return float((h/3)*(top_area + bottom_area + (math.sqrt(top_area*bottom_area))))

def get_volume(s1, s2, h):
    ta = area_square(s1)
    ba = area_square(s2)
    vol = vol_frustum(ta, ba, h)
    return round(vol, 3)