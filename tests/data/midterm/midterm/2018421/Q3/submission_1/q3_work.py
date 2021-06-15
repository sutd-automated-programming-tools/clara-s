# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area=s**2
    return area
#print(area_square(4))
    
def vol_frustum(top_area, bottom_area, height):
    volume=(height/3)*(top_area+bottom_area+math.sqrt(top_area*bottom_area))
    return volume
#print(vol_frustum(10, 12,10))

def get_volume(s1, s2, height):
    top_area=area_square(s1)
    bottom_area=area_square(s2)
    final_vol=vol_frustum(top_area, bottom_area, height)
    final_vol=round(final_vol,3)
    return final_vol


