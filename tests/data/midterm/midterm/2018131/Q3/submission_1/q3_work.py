# MID-TERM EXAM: QUESTION 3

import math


def area_square(s):
    area=s**2
    return area

def vol_frustum(top_area,bottom_area,height):
    v=(height/3)*(top_area+bottom_area+math.sqrt(top_area*bottom_area))
    return v

def get_volume(s1,s2,height):
    toparea=area_square(s1)
    bottomarea=area_square(s2)
    
    v=vol_frustum(toparea,bottomarea,height)
    return v