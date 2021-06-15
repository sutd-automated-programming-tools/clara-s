# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    ans=s**2
    return ans

def vol_frustum(top_area, bottom_area, height):
    con1=height/3
    con2=top_area+bottom_area
    con3=math.sqrt(top_area * bottom_area)
    ans = con1*(con2+con3)
    return ans

def get_volume(s1, s2, height):
    a1=area_square(s1)
    a2=area_square(s2)
    vol=vol_frustum(a1, a2, height)
    return vol
