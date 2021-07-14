# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s*s
    return area 

def vol_frustum(top_area, bottom_area, height):
    ta = top_area
    ba = bottom_area
    h = height 
    
    return round(((h/3) * (ta + ba + (ta*ba)**0.5)),3)


def get_volume(s1, s2, height):
    
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    
    answer = vol_frustum(top_area,bottom_area,height)
    return answer 