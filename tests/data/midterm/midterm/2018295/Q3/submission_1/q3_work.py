# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area=s*s
    return area

def vol_frustum(top_area, bottom_area, height):
    volume=(height/3)*(top_area+bottom_area+math.sqrt(top_area*bottom_area))
    return volume

def get_volume(s1, s2, height):
    top=area_square(s1)
    bottom=area_square(s2)
    volume=vol_frustum(top,bottom,height)
    return volume