# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s * s
    return area

def vol_frustum(top_area,bottom_area,height):
    part1 = height / 3
    part2 = math.sqrt(top_area * bottom_area)
    part3 = top_area + bottom_area
    volume = part1 * (part2 + part3)
    return volume


def get_volume(s1,s2,height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    final = vol_frustum(top_area,bottom_area,height)
    return final
