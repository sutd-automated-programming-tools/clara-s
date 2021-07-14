# MID-TERM EXAM: QUESTION 3

import math


def area_square(s):
    return s**2


def vol_frustum(top_area,bottom_area,height):
    h=height
    a1=top_area
    a2=bottom_area
    volume= h/3*(a1+a2+math.sqrt(a1*a2))
    return volume

def get_volume(s1,s2,height):
    a1= area_square(s1)
    a2= area_square(s2)
    volume = vol_frustum(a1,a2,height)
    volume= round(volume,3)
    return volume

