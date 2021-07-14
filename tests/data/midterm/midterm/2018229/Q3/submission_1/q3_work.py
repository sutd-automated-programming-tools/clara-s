# MID-TERM EXAM: QUESTION 3

import math
def area_square(s):
    s = float(s)
    area = s**2 
    return area
#print(area_square(2))
def vol_frustum(A1, A2, H):
    H = float(H)
    volume = (H/3) * (A1 + A2 + math.sqrt(A1 * A2))
    volume = float(volume)
    return volume
#print(vol_frustum(1,4,2))
def get_volume(s1,s2,H):
    A1 = area_square(s1)
    A2 = area_square(s2)
    Vol = vol_frustum(A1,A2,H)
    return round(Vol,3)
#print(get_volume(1,2,2))