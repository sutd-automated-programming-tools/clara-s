# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    squarearea=s**2
    squarearea=float(squarearea)
    squarearea=round(squarearea,3)
    return squarearea

def vol_frustum(top_area, bottom_area, height):
    vol=(height/3)*(top_area+bottom_area+math.sqrt(top_area*bottom_area))
    vol=round(vol,3)
    return vol

def get_volume(s1, s2, height):
    top_area= area_square(s1)
    bottom_area=area_square(s2)
    vol2=(height/3)*(top_area+bottom_area+math.sqrt(top_area*bottom_area))
    vol2=round(vol2,3)
    return vol2
    
