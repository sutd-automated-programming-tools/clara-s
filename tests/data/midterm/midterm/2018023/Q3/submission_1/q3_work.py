# MID-TERM EXAM: QUESTION 3
import math
def area_square(s):
    return s*s
def vol_frustum(top_area, bottom_area,height):
    constant = height/3
    squareroot = math.sqrt(top_area * bottom_area)
    volume = constant * (squareroot + top_area + bottom_area)
    return volume
def get_volume(s1,s2,height):
    A1 = area_square(s1)
    A2 = area_square(s2)
    finalvolume = vol_frustum(A1,A2,height)
    return round(finalvolume,3)

    