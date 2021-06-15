# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    side = float(input("Enter a side of the square: "))
    area = side*side
    return round(area,3)

def vol_frustum(top_area, bottom_area, height):
    a = (top_area*bottom_area)**0.5
    vol = (height/3) * (top_area+bottom_area+a)
    return round(float(vol),3)

def get_volume(s1, s2, height):
    s1,s2 = area_square(s)
    s1 = top_area
    s2 = bottom_area
    volume = vol_frustum(top_area, bottom_area, height)
    return volume
