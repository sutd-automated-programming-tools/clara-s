# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area=s**2
    return area


def vol_frustum(top_area,bottom_area,height):
    vol=(height/3)*(bottom_area + top_area + (top_area*bottom_area)**0.5)
    return vol

    
def get_volume(s1,s2,height):
    top_area=area_square(s1)
    bottom_area=area_square(s2)
    v= vol_frustum(top_area,bottom_area,height)
    return round(v,3)