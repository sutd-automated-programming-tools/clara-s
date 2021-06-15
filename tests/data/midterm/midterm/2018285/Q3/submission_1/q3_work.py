# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s*s

#print('{:.3f}'.format(area_square(3)))
#b
from math import sqrt
def vol_frustum(top_area,bottom_area,height):
    vol = (height/3)*(top_area + bottom_area + sqrt(top_area*bottom_area))
    return vol
#print('{:.3f}'.format(vol_frustum(1,4,2)))

#c
def get_volume(s1,s2,height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    return round(vol_frustum(top_area,bottom_area,height),3)
