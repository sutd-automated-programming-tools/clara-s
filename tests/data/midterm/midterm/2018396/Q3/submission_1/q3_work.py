# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area=s*s
    return(area)

def vol_frustum(top_area, bottom_area, height):
    H=height
    A1=top_area
    A2=bottom_area
    volume=(H/3)*(A1+A2+ math.sqrt(A1+A2))
    return(volume)

def get_volume(s1, s2, height):
    A1=area_square(s1)
    A2=area_square(s2)
    vol= vol_frustum(A1,a2,H)
    
    return(round(vol,2))
