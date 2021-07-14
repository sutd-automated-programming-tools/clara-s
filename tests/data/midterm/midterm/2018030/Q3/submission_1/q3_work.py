# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    A = s*s
    return A

def vol_frustum(top_area, bottom_area, height):
    V = (height/3)*(top_area+bottom_area+(math.sqrt(top_area*bottom_area)))
    return V

def get_volume(s1, s2, height):
    TopArea = area_square(s1)
    BottomArea = area_square(s2)
    V = vol_frustum(TopArea,BottomArea,height)
    return round(V,3)
    