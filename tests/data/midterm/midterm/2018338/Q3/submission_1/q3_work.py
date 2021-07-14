# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    result=s**2
    return result

def vol_frustum(top_area, bottom_area, height):
    vol=height*(top_area+bottom_area+math.sqrt(top_area*bottom_area))/3
    return vol
  

def get_volume(s1, s2, height):
    top=area_square(s1)
    bottom=area_square(s2)
    vol=vol_frustum(top,bottom,height)
    return vol
   
