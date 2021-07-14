#3
import math

def area_square(s):
    area = s**2
    return area

def vol_frustum(top_area, bottom_area, height):
    A1 = top_area
    A2 = bottom_area
    h = height
    vol = (h/3)*(A1 + A2 + (math.sqrt(A1 * A2)))
    return vol

def get_volume(s1, s2, height):
    if s = s1:
        A1 = area
        return A1
    if s = s2:
        A2 = area
        return A2
    get_volume = vol
    return round(get_volume, 3)



    
