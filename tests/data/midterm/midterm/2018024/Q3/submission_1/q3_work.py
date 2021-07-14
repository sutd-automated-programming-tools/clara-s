# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area=s**2
    return (round(area,3))
def vol_frustum(top_area,bottom_area,height):
    vol=(height/3)*(top_area+bottom_area+(math.sqrt(top_area*bottom_area)))
    return (round(vol,3))
def get_volume(s1,s2,height):
    top=area_square(s1)
    bottom=area_square(s2)
    v=vol_frustum(top,bottom,height)
    return (round(v,3))