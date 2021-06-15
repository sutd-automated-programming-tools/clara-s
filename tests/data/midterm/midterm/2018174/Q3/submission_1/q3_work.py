# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s**2
    return area

def vol_frustum(top_area, bottom_area, height):
    volume = (height/3)(top_area + bottom_area + math.sqrt(top_area * bottom_area))
    volume = int(float(volume))
    poop = round(volume,3)
    return poop 
   

def get_volume(s1, s2, height):
    s1 = area_square(s1)
    s2 = area_square(s2)
    volume2 = vol_frustrum(s1,s2,height)
    return volume2 
    
