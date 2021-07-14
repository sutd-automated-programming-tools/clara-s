# MID-TERM EXAM: QUESTION 3

import math
rt = math.sqrt
def area_square(s):
    return s*s

#print(area_square(2))

def vol_frustum(top_area, bottom_area, height):
    tA = top_area
    bA = bottom_area
    vol = (height/3)*(tA + bA + rt(tA*bA))
    return vol

def get_volume(s1,s2,height):
    tA = area_square(s1)
    bA = area_square(s2)
    vol = vol_frustum(tA,bA,height)
    return round(vol,3)
