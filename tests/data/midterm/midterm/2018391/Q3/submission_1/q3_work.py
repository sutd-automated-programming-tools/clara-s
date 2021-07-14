# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area_square=s**2
    return (area_square(s))

def vol_frustum(top_area, bottom_area, height):
    vol_frustum=height/3*(top_area+bottom_area+math.sqrt(top_area*bottom_area))
    return (vol_frustum(top_area, bottom_area, height)

def get_volume(s1, s2, height):
    get_volume=height/3*(s1**2+s2**2+math.sqrt(s1**2*s2**2))
    return (round(get_volume(s1, s2, height),3)
