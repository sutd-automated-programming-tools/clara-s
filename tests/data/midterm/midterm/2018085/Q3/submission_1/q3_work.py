# MID-TERM EXAM: QUESTION 3

import math
def area_square(s):
    return s**2
def vol_frustum(top,bottom,height):
    volume=(height/3)*(top+bottom+math.sqrt(top*bottom))
    return volume
def get_volume(s1,s2,height):
    top=area_square(s1)
    bottom=area_square(s2)
    volume=vol_frustum(top,bottom,height)
    return round(volume,3)
