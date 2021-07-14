
import math

def area_square(s):
    return s**2

def vol_frustum(top_area, bottom_area, height):
    
    return height*(top_area+bottom_area+(top_area*bottom_area)**0.5)/3

def get_volume(s1, s2, height):
    
    return vol_frustum(area_square(s1),area_square(s2),height)
