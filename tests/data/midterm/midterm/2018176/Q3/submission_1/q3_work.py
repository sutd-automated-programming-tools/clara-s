# MID-TERM EXAM: QUESTION 3

import math
def area_square(s):
    sqarea=s*s
    return sqarea

def vol_frustum(top_area,bottom_area,height):
    Volume=height/3*(top_area+bottom_area+math.sqrt(top_area*bottom_area))
    return Volume

def get_volume(s1,s2,height):
    top_area=area_square(s1)
    bottom_area=area_square(s2)
    ans=vol_frustum(top_area,bottom_area,height)
    ans=round(ans,3)
    return ans