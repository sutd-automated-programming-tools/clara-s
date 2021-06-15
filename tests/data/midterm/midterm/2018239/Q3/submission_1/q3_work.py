# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return round(s*s,3)
    pass

def vol_frustum(top_area, bottom_area, height):
    volume=height/3*(top_area+bottom_area+math.sqrt(top_area*bottom_area))
    return round(volume,3)
    pass

def get_volume(s1, s2, height):
    area1=area_square(s1)
    area2=area_square(s2)
    volume=vol_frustum(area1,area2,height)
    return round(volume,3)
    
    pass
