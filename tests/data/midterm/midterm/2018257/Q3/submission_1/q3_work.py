# MID-TERM EXAM: QUESTION 3

import math
def area_square(s):
    area = s**2
    return area

def vol_frustum(top_area, bottom_area, height):
    volume = height / 3 * ( top_area + bottom_area + math.sqrt(top_area*bottom_area))
    return volume

def get_volume(s1,s2,height):
    A1 = area_square(s1)
    A2 = area_square(s2)
    volume = height/3 *(A1 + A2 + math.sqrt(A1*A2))
    if volume == vol_frustum(A1,A2,height):
        return round(volume,3)