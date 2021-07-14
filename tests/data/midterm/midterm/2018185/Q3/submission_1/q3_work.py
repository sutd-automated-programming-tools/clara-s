# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    a=s**2
    return round(a,3)

def vol_frustum(top_area, bottom_area, height):
    V=((float(height)/3))*((float(top_area+bottom_area))+((float(top_area*bottom_area))**0.5))
    return V            

def get_volume(s1, s2, height):
    ars=area_square(s)
    
    
    
    
