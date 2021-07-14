# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s * s
    return area

def vol_frustum(top_area, bottom_area, height):
    volume = (height/3) * ((top_area + bottom_area) + math.sqrt(top_area * bottom_area))
    return volume

def get_volume(s1, s2, height):
    area_1 = area_square(s1)
    area_2 = area_square(s2)
    volume = vol_frustum(area_1, area_2, height)
    return volume
    
    pass
