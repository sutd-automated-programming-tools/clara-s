# MID-TERM EXAM: QUESTION 3

from math import sqrt

def area_square(s):
    areasquare = s*s
    return float(areasquare)

def vol_frustum(top_area, bottom_area, height):
    volume = height/3(top_area + bottom_area + sqrt(top_area*bottom_area ))
    return float(volume)

def get_volume(s1, s2, height):
    
    A1 = area_square(s1)
    A2 = area_square(s2)
    Vol = vol_fustram(A1,A2,height)
    
    round (Vol,3)
