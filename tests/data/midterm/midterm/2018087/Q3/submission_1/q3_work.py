# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s*s

def vol_frustum(top_area, bottom_area, height):
    vol = (height/3)*((top_area)+(bottom_area)+(math.sqrt(top_area * bottom_area)))
    return vol

def get_volume(s1,s2,height):
    top_area = s1*s1
    bottom_area = s2*s2
    vol = (height/3)*((top_area)+(bottom_area)+(math.sqrt(top_area * bottom_area)))#which is the same as part b
    return round(vol,3)