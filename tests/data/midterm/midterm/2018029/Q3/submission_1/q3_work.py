# MID-TERM EXAM: QUESTION 3
'''
import math

def area_square(s):
    pass

def vol_frustum(top_area, bottom_area, height):
    
    pass

def get_volume(s1, s2, height):
    
    pass
'''

import math

def area_square(s):
    area=s**2
    return area
    

def vol_frustum(top_area, bottom_area, height):
    vol=(height/3)*((top_area+bottom_area)+math.sqrt(top_area*bottom_area))
    return vol

def get_volume(s1, s2, height):
    A1=area_square(s1)
    A2=area_square(s2)
    Vol=(height/3)*((A1+A2)+math.sqrt(A1*A2))
    return round(Vol,3)