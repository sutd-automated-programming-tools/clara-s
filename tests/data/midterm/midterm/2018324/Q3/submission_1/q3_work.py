# MID-TERM EXAM: QUESTION 3

import math
def area_square(s):
    area = s * s
    return area

def vol_frustum(top_area, bottom_area, height):
    volume = (height/3) * (top_area + bottom_area + math.sqrt(top_area*bottom_area))
    return volume

def get_volume(s1, s2, height):
    toparea = area_square(s1)
    btmarea = area_square(s2)
    volume = vol_frustum(toparea, btmarea, height)
    return round(volume, 3)
