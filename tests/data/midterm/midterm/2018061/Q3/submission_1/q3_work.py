# MID-TERM EXAM: QUESTION 3

from math import *    
def area_square(s):
    area = s**2
    return area
def vol_frustum(top_area,bottom_area,height):
    height_frustum = height/3
    A1 = top_area
    A2 = bottom_area
    volume = height_frustum *(A1+A2+sqrt(A1*A2))
    return volume 
def get_volume(s1,s2,height):
    a = area_square(s1)
    b = area_square(s2)
    c = vol_frustum(a,b,height)
    return round(c,3)
