# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s*s
    return area
    
def vol_frustum(top_area, bottom_area, height):
    x = height/3
    y = math.sqrt(top_area * bottom_area) 
    vol = x * (top_area + bottom_area + y)
    return vol
    
def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)    
    volume = round(vol_frustum(top_area,bottom_area,height),3)
    return volume
    
