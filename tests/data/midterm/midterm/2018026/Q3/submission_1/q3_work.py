# MID-TERM EXAM: QUESTION 3

from math import sqrt

def area_square(s):
    area=s*s
    return area

def vol_frustum(top_area, bottom_area, height):
    vol= (height/3)*(top_area+bottom_area+sqrt(top_area*bottom_area))
    return vol
    
def get_volume(s1, s2, height):
    top_area= area_square(s1)
    bottom_area=area_square(s2)
    volans= vol_frustum(top_area, bottom_area, height)
    return volans
