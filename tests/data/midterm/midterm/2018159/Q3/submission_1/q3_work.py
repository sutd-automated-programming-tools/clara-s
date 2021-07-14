# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s**2
    return area

#print(area_square(2))

def vol_frustum(top, bottom, height):
    volume = (height*(top + bottom + math.sqrt(top*bottom)))/3 
    return volume

#print(vol_frustum(1,4,2))

def get_volume(s1, s2, height):
    top = area_square(s1)
    bottom = area_square(s2)
    volume = vol_frustum(top, bottom, height)
    return round(volume,3)

#print(get_volume(1.5,3.3,5.0))
