# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return (s*s)

def vol_frustum(top_area, bottom_area, height):
    result = (height/3)*(top_area + bottom_area + (top_area*bottom_area)**0.5)
    return round(result,3)
    

def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    result = vol_frustum(top_area,bottom_area,height)
    return round(result,3)
    
