# MID-TERM EXAM: QUESTION 3

import math
def area_square(s):
    return s**2
print (area_square(2))

def vol_frustum (top_area, bottom_area, height):
    a = math.sqrt(top_area*bottom_area)
    return (height/3)*(top_area + bottom_area + a)


def get_volume(s1, s2, height):
    A1 = area_square (s1)
    A2 = area_square (s2)
    v = vol_frustum (A1, A2 , height)
    return round(v,3)
