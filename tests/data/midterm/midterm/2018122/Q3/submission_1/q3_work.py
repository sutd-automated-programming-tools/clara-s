# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    ans = s ** 2
    return ans

def vol_frustum(top_area, bottom_area, height):
    area_part = (top_area + bottom_area + math.sqrt(top_area * bottom_area))
    ans_raw = (height / 3) * area_part
    return ans_raw

def get_volume(s1, s2, height):
    top_area_g = area_square(s1)
    bottom_area_g = area_square(s2)
    ans_get = (vol_frustum(top_area_g, bottom_area_g, height))
    final_ans = round(ans_get,3)
    return final_ans
