# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s*s
    return area

def vol_frustum(top_area, bottom_area, height):
    
    vol = (height/3)*(top_area + bottom_area + math.sqrt(top_area * bottom_area))
    return vol

def get_volume(s1, s2, height):
    
    area1 = area_square(s1)
    area2 = area_square(s2)
    vol = vol_frustum(area1, area2, height)
    return vol