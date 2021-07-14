# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s**2

def vol_frustum(top_area, bottom_area, height):
    product = top_area*bottom_area
    root = math.sqrt(product)
    summed = top_area + bottom_area + root
    return height*summed/3

def get_volume(s1, s2, height):
    area1 = area_square(s1)
    area2 = area_square(s2)
    volume = vol_frustum(area1, area2, height)
    return round(volume, 3)