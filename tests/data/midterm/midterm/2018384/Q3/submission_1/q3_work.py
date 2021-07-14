# MID-TERM EXAM: QUESTION 3

import math
n=math.sqrt


def area_square(s):
   
    areasq=round(s**2,3)
    return areasq

def vol_frustum(top_area, bottom_area, height):
    ta=float(top_area)
    ba=float(bottom_area)
    h=float(height)
    Volume=(h/3)*(ta+ba+n(ta*ba))
    return round(Volume,3)

def get_volume(s1, s2, height):
    
    top_area=area_square(s1)
    bottom_area=area_square(s2)
    Volume=vol_frustum(top_area, bottom_area, height)
    return Volume                 
