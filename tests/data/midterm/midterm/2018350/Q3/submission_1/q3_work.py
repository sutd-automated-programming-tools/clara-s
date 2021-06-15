# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return float(s**2)
#print("{:.3f}".format(area_square(3)))

def vol_frustum(top_area, bottom_area, height):
    a1 = float(top_area)
    a2 = float(bottom_area)
    h = float(height)
    ans = (h/3)*(a1 + a2 + math.sqrt(a1*a2))
    return ans
#print("{:.3f}".format(vol_frustum(2,2,2)))

def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    ans = vol_frustum(top_area,bottom_area,height)
    return round(ans,3)
#print("{:.3f}".format(get_volume(3.6,6.4,4.0)))