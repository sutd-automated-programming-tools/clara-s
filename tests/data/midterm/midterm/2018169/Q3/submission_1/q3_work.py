# MID-TERM EXAM: QUESTION 3

#import math

#def area_square(s):
 #   pass

#def vol_frustum(top_area, bottom_area, height):
    
 #   pass

#def get_volume(s1, s2, height):
    
 #   pass

import math
def area_square(s):
    return s**2
def vol_frustum(top_area,bottom_area,height):
    A1 = top_area
    A2 = bottom_area
    volume = (height/3)*(A1 + A2 + math.sqrt(A1*A2))
    return volume
def get_volume(s1,s2,height):
    A1 = area_square(s1)
    A2 = area_square(s2)
    return (height/3)*(A1 + A2 + math.sqrt(A1*A2))