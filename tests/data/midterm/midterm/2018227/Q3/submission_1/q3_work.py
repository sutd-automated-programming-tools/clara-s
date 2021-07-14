# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s*s

def vol_frustum(top_area, bottom_area, height):
    ans=(height/3)*(top_area+bottom_area+math.sqrt(top_area*bottom_area))
    return ans

def get_volume(s1, s2, height):
    
    top_area=area_square(s1)
    bottom_area=area_square(s2)
    vol=vol_frustum(top_area, bottom_area, height)
    vol=round(vol,3)
    return vol
