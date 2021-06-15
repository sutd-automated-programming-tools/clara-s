# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    A = s ** 2
    return A
#print(area_square(2))
    
def vol_frustum(A1,A2,H):
    volume = (H/3) * (A1 + A2 + math.sqrt(A1 * A2)) 
    return volume
#print(vol_frustum(1,4,2))
    
def get_volume(s1,s2,H):
    A1 = area_square(s1)
    A2 = area_square(s2)
    final_volume = vol_frustum(A1,A2,H)
    return final_volume