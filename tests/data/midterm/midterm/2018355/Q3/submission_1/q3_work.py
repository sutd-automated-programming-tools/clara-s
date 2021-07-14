# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    area = s**2
    return (area)

def vol_frustum(top_area, bottom_area, height):
    part_1 = height/3
    part_2 = math.sqrt(top_area*bottom_area)
    vol = part_1*(top_area + bottom_area + part_2)
    vol = '{:.3f}'.format(vol)
    return (float(vol))

def get_volume(s1, s2, height):
    
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    ans = vol_frustum(top_area, bottom_area, height)
    ans = '{:.3f}'.format(ans)
    return (float(ans))
