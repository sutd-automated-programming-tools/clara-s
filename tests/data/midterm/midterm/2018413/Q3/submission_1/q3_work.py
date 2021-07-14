# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    ass=float(s*s)
    return ass

def vol_frustum(top_area, bottom_area, height):
    volume= float((float(height)/3) * (top_area + bottom_area + float(math.sqrt(top_area*bottom_area))))
    return volume
    pass

def get_volume(s1, s2, height):
    top_area= float(area_square(s1))
    bottom_area= float(area_square(s2))
    answer= round(float(vol_frustum(top_area, bottom_area, height)), 3)
    return answer
    pass
