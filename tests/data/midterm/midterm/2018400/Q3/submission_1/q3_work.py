# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s**2

def vol_frustum(top_area,bottom_area,height):
    h=height
    t=top_area
    b=bottom_area
    return (h/3)*(t+b+(math.sqrt(t*b)))
                  
def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area  = area_square(s2)
    return round(vol_frustum(top_area,bottom_area,height),3)
