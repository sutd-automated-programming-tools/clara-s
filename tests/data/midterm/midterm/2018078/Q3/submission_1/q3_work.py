# MID-TERM EXAM: QUESTION 3
from math import sqrt    
def area_square(s):
    A=s*s
    return A 

def vol_frustum(top_area,bottom_area,height):
    volume=height/3*(top_area+bottom_area+sqrt(top_area*bottom_area))
    return volume

def get_volume(s1,s2,height):
    A1=area_square(s1)
    A2=area_square(s2)
    getting_volume=vol_frustum(A1,A2,height)
    return getting_volume