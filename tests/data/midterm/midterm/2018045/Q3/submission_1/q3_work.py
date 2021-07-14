# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s*s
    return area

def volume_frustrum(top, bottom, h):
    volume = (h/3)*((top+bottom)+math.sqrt(top*bottom))
    return volume

def get_volume(s1,s2,height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    volume = volume_frustrum(top_area, bottom_area, height)
    volume = round(volume,3)
    return volume