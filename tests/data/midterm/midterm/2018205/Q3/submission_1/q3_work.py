# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    a = s*s
    #ans = '{:.3f}'.format(a)
    return a

print(area_square(2))
print(area_square(3))

def vol_frustum(top_area, bottom_area, height):
    a1 = top_area
    a2 = bottom_area
    h = height
    
    v = (h/3)* (a1 + a2 + math.sqrt(a1*a2))
    ans = '{:.3f}'.format(v)
    return ans

print(vol_frustum(1, 4, 2))
print(vol_frustum(2, 2, 2))

def get_volume(s1, s2, height):
    top_area = area_square(s1)
    bottom_area = area_square(s2)
    
    v = vol_frustum(top_area, bottom_area, height)
    return v

print(get_volume(1, 3, 4))
