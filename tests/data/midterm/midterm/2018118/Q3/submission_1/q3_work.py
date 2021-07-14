# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return (s**2)

def vol_frustum(A1,A2,H):
    volume= (H/3)*(A1+A2+math.sqrt(A1*A2))
    return volume

def get_volume(s1,s2,H):
    A1=area_square(s1)
    A2=area_square(s2)
    volume=vol_frustum(A1,A2,H)
    return round(volume,3)
