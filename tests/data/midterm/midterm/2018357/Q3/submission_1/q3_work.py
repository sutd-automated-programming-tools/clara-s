# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return((s*s))

def vol_frustum(top_area, bottom_area, height):
    
    a = height/3
    b = top_area
    c = bottom_area
    d = math.sqrt(b*c)
    volume = a*(b + c + d)
    return(volume)

def get_volume(s1, s2, height):
    
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    h = height
    return(round(vol_frustrum(top_area, bottom_area, h)),3)
