# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s*s
    return area

def vol_frustum(top_area, bottom_area, height):
    root = (top_area*bottom_area)**(0.5)
    bracket = top_area + bottom_area + root
    volume = (height/3)*bracket
    return volume

def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    volume = vol_frustum(top_area, bottom_area, height)
    volume_3dp = round(volume,3)
    return volume_3dp
