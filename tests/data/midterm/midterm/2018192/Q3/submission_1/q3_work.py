import math

def area_square(s):
    return s*s

def vol_frustum(top_area, bottom_area, height):
    volume = (top_area + bottom_area + math.sqrt(top_area*bottom_area))*height/3
    return volume

def get_volume(s1, s2, height):
    a1 = area_square(s1)
    a2 = area_square(s2)
    h = height
    
    volume = vol_frustum(a1,a2,h)
    return round(volume, 3)