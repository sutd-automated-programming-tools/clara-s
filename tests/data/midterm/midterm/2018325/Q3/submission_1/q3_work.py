# MID-TERM EXAM: QUESTION 3

import math
from math import sqrt

def area_square(s):
    area = float(s**2)
    return area


def vol_frustum(top_area, bottom_area, height):
    vol = (height/3) * (top_area + bottom_area + (sqrt(top_area * bottom_area)))
    return round(vol,3)
    
   

def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    totvol = vol_frustum(top_area, bottom_area, height)
    return totvol
    
  

