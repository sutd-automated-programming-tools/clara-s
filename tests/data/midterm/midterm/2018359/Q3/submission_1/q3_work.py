# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s**2

def vol_frustum(top_area, bottom_area, height):
    Volume1= height/3
    Volume2= top_area +bottom_area
    Volume3= math.sqrt(top_area*bottom_area)
    Volume4= Volume1*(Volume2+Volume3)
    return Volume4

def get_volume(s1, s2, height):
    top_area=area_square(s1)
    bottom_area=area_square(s2)
    vol= vol_frustum(top_area, bottom_area, height)
    return round(vol,3)