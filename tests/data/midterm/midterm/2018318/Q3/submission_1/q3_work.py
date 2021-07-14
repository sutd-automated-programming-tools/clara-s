# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return (s**2)

def vol_frustum(top_area, bottom_area, height):
    a1=top_area
    a2=bottom_area
    h=height
    vol=(h/3)*(a1+a2+math.sqrt(a1*a2))
    return vol

def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    return (round(vol_frustum(top_area, bottom_area, height),3))
    
