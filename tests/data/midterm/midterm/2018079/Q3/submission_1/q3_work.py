# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s**2
    return area
  

def vol_frustum(top_area, bottom_area, height):
    third_H = height/3
    addition = top_area + bottom_area + (math.sqrt(top_area*bottom_area))
    volume = third_H * addition
    return volume
    

def get_volume(s1, s2, height):
    top = area_square(s1)
    bottom = area_square(s2)
    get_volume = vol_frustum(top, bottom, height)
    return get_volume
