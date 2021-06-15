# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return (s ** 2)

def vol_frustum(top_area, bottom_area, height):
    ans = (height / 3) * (top_area + bottom_area + sqrt(top_area * bottom_area))
    return ans


def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bot_area = area_square(s2)
    return (vol_frustum(top_area, bot_area, height))