# MID-TERM EXAM: QUESTION 3

import math
def area_square(s): #s is side of square
    return s**2

def vol_frustrum(top_area,bottom_area,height):
    ta = top_area
    ba = bottom_area
    h = height
    
    volume = (h/3) *(ta+ba + math.sqrt(ta*ba))
    return volume

def get_volume(s1,s2,height):
    A1 = area_square(s1)
    A2 = area_square(s2)
    vol = vol_fulstrum(A1,A2,height)
    return vol