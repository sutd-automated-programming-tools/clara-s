# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s*s
    return (area)

def vol_frustum(top_area, bottom_area, height):
    vol = (height/3.0)*(top_area+bottom_area+ (math.sqrt(bottom_area*top_area)))
    return (vol)
    

def get_volume(s1, s2, height):
    top = area_square(s1)
    bot = area_square(s2)
    vol = vol_frustum(top,bot, height)
    return (round (vol,3))
    
