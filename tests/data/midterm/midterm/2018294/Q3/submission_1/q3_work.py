# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s*s
    return area

def vol_frustrum(top_area, bottom_area, height):
    volume = (height/3)*(top_area + bottom_area + (math.sqrt(top_area*bottom_area)))
    return volume

def get_volume(s1, s2, height):
    x = area_square(s1)
    y = area_square(s2)
    return (float(vol_frustrum(x, y, height)))
