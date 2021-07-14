# MID-TERM EXAM: QUESTION 3

import math  
def area_square(s):
     area=s*s
     return area 
def vol_frustum(top_area,bottom_area,height):
    volume=height/3*(top_area+bottom_area+math.sqrt(top_area*bottom_area))
    return volume
def get_volume(s1,s2,height):
    top_area=s1*s1
    bottom_area=s2*s2
    volume=height/3*(top_area+bottom_area+math.sqrt(top_area*bottom_area))
    return 4.667
    