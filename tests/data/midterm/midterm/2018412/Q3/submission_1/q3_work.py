# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s * s
    area = '{:.3f}'.format(area)
    area = float(area)
    return area

def vol_frustum(top_area, bottom_area, height):
    vol = (height/3) * (top_area + bottom_area + math.sqrt(top_area * bottom_area))
    vol = '{:.3f}'.format(vol)
    vol = float(vol)
    return vol

def get_volume(s1, s2, height):
    top = area_square(s1)
    bottom = area_square(s2)
    volume = float(vol_frustum(float(top), float(bottom), height))
    volume = '{:.3f}'.format(volume)
    volume = float(volume)
    return volume
