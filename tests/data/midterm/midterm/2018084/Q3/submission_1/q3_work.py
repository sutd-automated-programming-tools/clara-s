# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area=s**2
    return area

def vol_frustum(top_area, bottom_area, height):
    volume= (height/3)*(top_area+bottom_area+(((top_area)*bottom_area)**(1/2)))
    return volume

def get_volume(s1, s2, height):
    return(vol_frustum(area_square(s1), area_square(s2), height))