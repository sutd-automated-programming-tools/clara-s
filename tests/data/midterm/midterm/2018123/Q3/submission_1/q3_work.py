# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    ans=s*s
    return ans
    

def vol_frustum(top_area, bottom_area, height):
    ans=(height/3)*(top_area+bottom_area+math.sqrt(top_area*bottom_area))
    return ans
    

def get_volume(s1, s2, height):
    ans=vol_frustum(area_square(s1), area_square(s2), height)
    ans=float(ans)
    ans=round(ans,3)
    return ans
