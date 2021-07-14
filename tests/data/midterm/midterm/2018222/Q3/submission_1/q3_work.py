# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    ans = s*s
    return ans

def vol_frustum(top_area, bottom_area, height):
    a = top_area
    b = bottom_area
    H = height
    volume = H/3*(a+b+math.sqrt((a*b)))
    return volume

def get_volume(s1, s2, height):
    
    area1 = area_square(s1)
    area2 = area_square(s2)
    volume1=vol_frustum(area1,area2,height)
    return round(volume1,3)
