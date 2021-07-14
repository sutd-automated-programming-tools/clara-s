# MID-TERM EXAM: QUESTION 3
import math as m

def area_square(s):
    area = s**2
    return area

def vol_frustum(top_area, bottom_area, height):
    vol = (height/3)*(top_area + bottom_area + m.sqrt(top_area + bottom_area))
    return round(vol,3)

def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    vol = vol_frustum(top_area, bottom_area, height)
    
    return vol