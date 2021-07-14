# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area=s*s
    return area

def vol_frustum(top_area, bottom_area, height):
    volume = (height/3)*(top_area + bottom_area +((top_area*bottom_area)**0.5))
    return volume
    
def get_volume(s1, s2, height):
    top_square=area_square(s1)
    bottom_square=area_square(s2)
    vol=vol_frustum(top_square, bottom_square, height)
    return vol
