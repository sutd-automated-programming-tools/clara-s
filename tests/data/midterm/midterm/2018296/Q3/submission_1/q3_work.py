# MID-TERM EXAM: QUESTION 3

import math
def area_square(s):
    a = s**2
    return float(a)
def vol_frustum(top_area, bottom_area, height):
    top_area = float(top_area)
    bottom_area = float(bottom_area)
    height = float(height)

    vol = (height/3)*(top_area + bottom_area + math.sqrt(top_area*bottom_area))
    
    return vol

def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    
    volume = vol_frustum(top_area, bottom_area, height)
    volume = round(volume, 3)
    return volume


print(vol_frustum(1,4,2))