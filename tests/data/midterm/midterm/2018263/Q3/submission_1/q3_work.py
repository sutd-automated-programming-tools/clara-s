# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    a=s**2
    return a
    pass

def vol_frustum(top_area, bottom_area, height):
    v=height/3.0*(top_area+bottom_area+math.sqrt(top_area*bottom_area))
    return round(v,3)
    pass

def get_volume(s1, s2, height):
    t=area_square(s1)
    b=area_square(s2)
    vo=vol_frustum(t,b,height)
    return round(vo,3)
    pass
