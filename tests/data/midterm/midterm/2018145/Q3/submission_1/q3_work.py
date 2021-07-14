# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s*s

def vol_frustum(top_area, bottom_area, height):
    area_term = top_area + bottom_area + math.sqrt(top_area*bottom_area)
    volume = (height/3)*area_term
    return volume

def get_volume(s1, s2, height):
    area1 = area_square(s1)
    area2 = area_square(s2)
    volume = vol_frustum(area1,area2,height)
    return volume
    
