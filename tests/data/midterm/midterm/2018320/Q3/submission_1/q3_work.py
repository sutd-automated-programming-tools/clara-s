# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s*s

def vol_frustum(top_area, bottom_area, height):
    
    a=top_area
    b=bottom_area
    vol=(height/3.0)*(a+b+math.sqrt(a*b))
    return vol

def get_volume(s1, s2, height):
    
    a=area_square(s1)
    b=area_square(s2)
    
    vol=vol_frustum(a,b,height)
    return round(vol,3)

