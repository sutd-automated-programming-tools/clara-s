# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area=s*s
    return area

def vol_frustum(top_area, bottom_area, height):
    A1=top_area
    A2=bottom_area
    H=height
    A1A2=A1*A2
    vol=(H/3)*(A1+A2+math.sqrt(A1A2))
    return vol
    

def get_volume(s1, s2, height):
    top_area=area_square(s1)
    bottom_area=area_square(s2)
    return vol_frustum(top_area,bottom_area,height)
    
    
