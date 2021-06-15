# MID-TERM EXAM: QUESTION 3

import math
def area_square(s):
    area = s*s
    area = round(area,3)
    return (area)



def vol_frustum(top_area,bottom_area, height):
    a1 = top_area
    a2 = bottom_area
    h = height
    
    volume = (h/3)*(a1 + a2 + math.sqrt(a1*a2))
    volume = round(volume,3)
    return volume

def get_volume(s1, s2, height):
    a1 = area_square(s1)
    a2 = area_square(s2)
    vol = vol_frustum(a1,a2,height)
    ans = round(vol,3)
    return ans
