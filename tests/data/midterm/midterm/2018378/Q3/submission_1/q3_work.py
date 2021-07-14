# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s**2

def vol_frustrum(top,bottom,height):
    return (height/3)*(top+bottom+math.sqrt(top*bottom))

def get_volume(s1,s2,height):
    top=area_square(s1)
    bottom=area_square(s2)
    return vol_frustrum(top,bottom,height)
