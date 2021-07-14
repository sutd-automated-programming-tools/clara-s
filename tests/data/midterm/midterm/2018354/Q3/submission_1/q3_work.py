# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area=s**2
    return round(float(area),4)

def vol_frustum(top_area, bottom_area, height):
    
    volume=height/3*(top_area+bottom_area+(top_area*bottom_area)**0.5)
    return round(float(volume),4)

def get_volume(s1, s2, height):
    
    val= vol_frustum(area_square(s1),area_square(s2), height)
    return round(float(val), 3)

