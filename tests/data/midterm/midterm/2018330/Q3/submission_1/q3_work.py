# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area=s**2
    return area
    pass

def vol_frustum(top_area, bottom_area, height):
    h=height
    ba=bottom_area
    ta=top_area
    vol=(h/3)*(ta+ba+(ta*ba)**(0.5))
    return vol
    
    pass

def get_volume(s1, s2, height):
    ta=area_square(s1)
    ba=area_square(s2)
    h=height
    
    vol2=vol_frustum(ta, ba, h)
    return vol2
    
    pass
