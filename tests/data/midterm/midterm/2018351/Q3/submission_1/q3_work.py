# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s **2
    return area

def vol_frustum(top_area, bottom_area, height):
    volume = 1/3*height * (top_area + bottom_area + math.sqrt(top_area * bottom_area))
    return volume

def get_volume(s1, s2, height):
    area1 = s1**2
    area2 = s2**2
    vol_frustum = 1/3* height * (area1 + area2 + math.sqrt(area1 * area2))                  
    vol_frustum = round(vol_frustum,3)
    
    return vol_frustum