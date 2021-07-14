# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s * s
    return area

def vol_frustum(top_area, bottom_area, height):
    s1 = height/3
    s2 = top_area + bottom_area + math.sqrt(top_area * bottom_area)
    ans = s1 * s2
    return ans

def get_volume(s1, s2, height):
    
    top_area = area_square(s1)
    bot_area = area_square(s2)
    ans2 = vol_frustum (top_area, bot_area, height)
    return ans2
    
