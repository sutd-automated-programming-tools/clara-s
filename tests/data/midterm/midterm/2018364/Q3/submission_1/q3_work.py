# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return(s**2)

def vol_frustum(top_area, bottom_area, height):
    ans = top_area + bottom_area + math.sqrt(top_area * bottom_area)
    ans = ans * height
    ans = ans/3
    ans = float(ans)
    
    return (ans)

def get_volume(s1, s2, height):
    a1 = area_square(s1)
    a2 = area_square(s2)
    
    ans = vol_frustum(a1, a2, height)
    ans = float(ans)
    ans = round(ans,3)
    
    return (ans)
