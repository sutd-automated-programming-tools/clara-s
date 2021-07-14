# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area=s**2
    return area
    pass


def vol_frustrum(top_area, bottom_area, height):
    H=height
    A1=top_area
    A2=bottom_area
    
    volume= (H/3)*(A1+A2+math.sqrt(A1*A2))
    return volume
    pass


def get_volume(s1, s2, height):
    A1=area_square(s1)
    A2=area_square(s2)
    
    top_area=A1
    bottom_area=A2
    
    vol= vol_frustrum(top_area, bottom_area, height)
    
    return vol