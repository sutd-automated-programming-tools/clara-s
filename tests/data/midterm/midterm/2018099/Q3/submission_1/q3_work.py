# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    areasq=s*s
    return (areasq)

def vol_frustum(top_area, bottom_area, height):
    totalarea=top_area+bottom_area+math.sqrt(top_area*bottom_area)
    vol=(height/3)*(totalarea)
    return (vol)

def get_volume(s1, s2, height):
    top_area= area_square(s1)
    bottom_area= area_square(s2)
    get= round(vol_frustum(top_area,bottom_area,height),3)
    return (get)
    