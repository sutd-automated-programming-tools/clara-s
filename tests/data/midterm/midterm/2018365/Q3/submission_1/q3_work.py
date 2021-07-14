# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    A=s*s
    print(A)
    return(A)

def vol_frustum(top_area, bottom_area, height):
    V=(height/3)*(top_area+bottom_area+(bottom_area*top_area)**0.5)
    return(V)
    
def get_volume(s1, s2, height):
    S1_Area=area_square(s1)
    S2_Area=area_square(s2)
    VOL=vol_frustum(S1_Area, S2_Area, height)
    return VOL
