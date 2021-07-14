# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    ans_area = s**2
    return ans_area

def vol_frustum(top_area, bottom_area, height):
    ans1_vol = height*(top_area + bottom_area + math.sqrt(top_area*bottom_area))/3
    return ans1_vol

def get_volume(s1, s2, height):
    a1 = area_square(s1)
    a2 = area_square(s2)
    final_volume = vol_frustum(a1, a2, height)
    return final_volume

